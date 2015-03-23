from zope.component import getMultiAdapter
try:
    from zope.component.hooks import getSite
except:
    from zope.app.component.hooks import getSite
from zope.globalrequest import getRequest

import schedule
import logging

logger = logging.getLogger('collective.schedule')


def scheduledirective(_context, view, unit, interval=None, at=None):

    logger.info("Job: '%(view)s' scheduled every %(interval)s%(unit)s %(at)s" % {
        'view': view,
        'interval': interval and ("%s " % interval) or "",
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

    if isinstance(view, unicode):
        view = view.encode('utf8')

    # wrapper function to trigger the view
    def load_view(viewname):
        context = getSite()
        request = getRequest()
        try:
            view = getMultiAdapter((context, request),
                                   name=viewname)
            view()
        except Exception:
            logger.exception('Exception whilst executing job: %s', viewname)

    # schedule the wrapper function
    jobtime.do(load_view, view)
