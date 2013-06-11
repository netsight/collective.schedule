from zope.component import getUtility
from Products.CMFCore.interfaces import ISiteRoot

import schedule
import logging

logger = logging.getLogger('collective.schedule')


def scheduledirective(_context, view, unit, interval=None, at=None):

    logger.info("Job: '%(view)s' scheduled every %(interval)s%(unit)s %(at)s" % {
        'view': view,
        'interval': interval or "",
        'unit': unit,
        'at': at and ("at %s" % at) or "",
    })
    if interval is None:
        interval = 1
    else:
        interval = int(interval)

    # build the job time from the arguments
    jobtime = getattr(schedule.every(interval), unit)
    if at is not None:
        jobtime = jobtime.at(at)

    def load_view(viewname):
        site = getUtility(ISiteRoot)
        site.restrictedTraverse(viewname)()

    jobtime.do(load_view, view)
