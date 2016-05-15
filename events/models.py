from django.db import models


class Event(models.Model):
    # What?
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    # Where?
    location = models.CharField(max_length=50)

    # When?
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)

    # Who?
    # TODO: contacts

    def __str__(self):
        return "%s (%s at %s)" % (self.title, self.start_date, self.start_time)
