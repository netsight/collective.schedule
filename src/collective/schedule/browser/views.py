import schedule
import logging

from Products.Five.browser import BrowserView

logger = logging.getLogger('collective.schedule')


class ScheduleTick(BrowserView):

    def tick(self):
        schedule.run_pending()
