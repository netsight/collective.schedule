from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class CollectiveSchedule(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import collective.schedule
        xmlconfig.file('configure.zcml',
                       collective.schedule,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        pass

COLLECTIVE_SCHEDULE_FIXTURE = CollectiveSchedule()
COLLECTIVE_SCHEDULE_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(COLLECTIVE_SCHEDULE_FIXTURE, ),
                       name="CollectiveSchedule:Integration")