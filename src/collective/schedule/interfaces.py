from zope.interface import Interface
from zope.schema import TextLine


class IScheduleDirective(Interface):
    """ Sets up a regular cron-like job
        This is a simple zcml interface to the python 'schedule' package
        https://pypi.python.org/pypi/schedule
    """

    view = TextLine(
        title=u"View",
        description=u"The name of the view or script to trigger.")

    unit = TextLine(
        title=u"Unit",
        description=u"The unit of frequency.")

    interval = TextLine(
        title=u"Interval",
        description=u"How often the job should be run.",
        required=False)

    at = TextLine(
        title=u"At Time",
        description=u"An optional time to run the job.",
        required=False)
