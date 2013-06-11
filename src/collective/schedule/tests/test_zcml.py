import unittest2 as unittest
from Zope2.App import zcml

import datetime
import schedule
import collective.schedule
from collective.schedule.testing import\
    COLLECTIVE_SCHEDULE_INTEGRATION_TESTING


class TestExample(unittest.TestCase):

    layer = COLLECTIVE_SCHEDULE_INTEGRATION_TESTING
    zcml_template = """
        <configure
        xmlns="http://namespaces.zope.org/zope"
        xmlns:schedule="http://namespaces.zope.org/schedule">
        %s
        </configure>
    """

    def setUp(self):
        zcml.load_config('meta.zcml', collective.schedule)

    def tearDown(self):
        schedule.clear()

    def test_hourly_job(self):
        zcml.load_string(self.zcml_template % '''
        <schedule:job
            view="foo"
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
            view="foo"
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
