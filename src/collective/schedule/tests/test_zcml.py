import unittest2 as unittest
from Zope2.App import zcml

import collective.schedule
from collective.schedule.testing import\
    COLLECTIVE_SCHEDULE_INTEGRATION_TESTING


class TestExample(unittest.TestCase):

    layer = COLLECTIVE_SCHEDULE_INTEGRATION_TESTING

    def setUp(self):
        # you'll want to use this to set up anything you need for your tests
        # below
        zcml.load_config('meta.zcml', collective.schedule)

    def test_job(self):
        zcml.load_string(
            '''<schedule:job name="foo" />''')
