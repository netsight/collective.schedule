import unittest2 as unittest
from Zope2.App import zcml
from Products.Five.browser import BrowserView

import datetime
import schedule
import collective.schedule
from collective.schedule.testing import\
    COLLECTIVE_SCHEDULE_INTEGRATION_TESTING

from plone.app.testing import SITE_OWNER_NAME
from plone.testing import z2

VIEW_MARKER = 'dummy-view-called'


class DummyView(BrowserView):
    """ dummy browser view that can be looked up at the root """
    def dummy(self):
        self.request.set(VIEW_MARKER, 1)


class TestZCML(unittest.TestCase):

    layer = COLLECTIVE_SCHEDULE_INTEGRATION_TESTING
    zcml_template = """
        <configure
        xmlns="http://namespaces.zope.org/zope"
        xmlns:schedule="http://namespaces.zope.org/schedule">
        %s
        </configure>
    """

    def setUp(self):
        self.app = self.layer['app']
        self.request = self.app.REQUEST
        zcml.load_config('meta.zcml', collective.schedule)
        zcml.load_config('test_view.zcml', collective.schedule.tests)

    def tearDown(self):
        schedule.clear()

    def test_hourly_job(self):
        zcml.load_string(self.zcml_template % '''
        <schedule:job
            view="dummy-view"
            unit="hour"
            />
        ''')

        jobs = schedule.jobs
        self.assertEquals(len(jobs), 1)
        job = jobs[0]
        self.assertEquals(job.interval, 1)
        self.assertEquals(job.unit, 'hours')
        self.assertEquals(job.at_time, None)

    def test_daily_job(self):
        zcml.load_string(self.zcml_template % '''
        <schedule:job
            view="dummy-view"
            unit="day"
            at="3:00"
            />
        ''')

        jobs = schedule.jobs
        self.assertEquals(len(jobs), 1)
        job = jobs[0]
        self.assertEquals(job.interval, 1)
        self.assertEquals(job.unit, 'days')
        self.assertEquals(job.at_time, datetime.time(3, 0))

        self.assertFalse(self.request.get(VIEW_MARKER))

        schedule.run_all()

        self.assertTrue(self.request.get(VIEW_MARKER))
