from datetime import datetime

from django.db import models
from django.utils.timezone import localtime


class Event(models.Model):
    # What?
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    # Where?
    location = models.CharField(max_length=50)

    # When?
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)

    # Who?
    # TODO: contacts/organizers

    def __str__(self):
        return "%(title)s (%(time)s)" % {
            "title": self.title,
            "time": " at ".join(Event.format_datetime(self.start_time))  # self.duration
        }

    @staticmethod
    def format_datetime(dt):
        date = datetime.strftime(localtime(dt), "%A, %B %d, %Y")
        time = datetime.strftime(localtime(dt), "%I:%M %p")
        yield from (date, time)

    @property
    def duration(self):
        """Returns a string representing the duration of the event"""
        dt = dict()
        dt["start_date"], dt["start_time"] = Event.format_datetime(self.start_time)
        if self.end_time:
            dt["end_date"], dt["end_time"] = Event.format_datetime(self.end_time)
            if self.start_time.date() == self.end_time.date():
                duration = "%(start_date)s, from %(start_time)s to %(end_time)s"
            else:
                duration = "%(start_date)s at %(start_time)s to %(end_date)s at %(end_time)s"
        else:
            duration = "%(start_date)s at %(start_time)s"
        return duration % dt
