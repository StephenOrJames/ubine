from datetime import datetime

from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.db import models
from django.template.loader import get_template
from django.utils.crypto import get_random_string
from django.utils.timezone import localtime


EMAIL_SENDER = "UBinE Events <events@ubine.ml>"

class Event(models.Model):
    # What?
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=5000)

    # Where?
    location = models.CharField(max_length=50)

    # When?
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)

    # Who?
    # TODO: contacts/organizers

    # Notifications
    # subscribers = models.ManyToManyField("Subscriber")

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

    def save(self, *args, **kwargs):
        subscribers = Subscriber.objects.filter(opted_in=True)
        for subscriber in subscribers.all():
            send_mail(
                "Event on UBinE: %s" % self.title,
                self.description,
                EMAIL_SENDER,
                [subscriber.email_address]
            )
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-start_time", "-end_time"]


class Subscriber(models.Model):
    """A subscriber is one who subscribes to events.

    Attributes:
        email_address: The email address of the subscriber.
        email_confirmed: If the subscriber has confirmed his/her email address.
        code: The last assigned confirmation/unsubscription code.
    """

    CODE_LENGTH = 25

    email_address = models.EmailField(unique=True)
    opted_in = models.BooleanField(default=False)
    code = models.CharField(max_length=CODE_LENGTH, unique=True)
    # code_updated = models.DateTimeField()  # TODO: update doc when enabled

    # TODO: add a way to allow users to limit their subscription

    def __str__(self):
        return self.email_address

    @staticmethod
    def build_url(request, view, code):
        return request.build_absolute_uri(
            reverse("events:%s" % view, args=(code,))
        )

    @classmethod
    def create(cls, email_address, request):
        if not Subscriber.objects.filter(email_address=email_address).exists():
            subscriber = cls(email_address=email_address)
            subscriber.save()
            if subscriber.code:
                body_text = get_template("events/emails/subscribe_confirm.txt")
                context = {
                    "url": Subscriber.build_url(request, "subscribe", subscriber.code)
                }
                return send_mail(
                    "UBinE Events Subscription Confirmation",
                    body_text.render(context),
                    EMAIL_SENDER,
                    [subscriber.email_address]
                )
        return False

    def opt_in(self, request):
        if not self.opted_in:
            self.opted_in = True
            self.generate_code()
            self.save()
            body_text = get_template("events/emails/subscribe_confirmed.txt")
            context = {
                "url": Subscriber.build_url(request, "unsubscribe", self.code)
            }
            return send_mail(
                "UBinE Events Subscription Confirmation",
                body_text.render(context),
                EMAIL_SENDER,
                [self.email_address]
            )
        return False

    def opt_out(self, request):
        if self.opted_in:
            self.opted_in = False
            self.generate_code()
            self.save()
            body_text = get_template("events/emails/unsubscribed.txt")
            context = {
                "url": Subscriber.build_url(request, "subscribe", self.code)
            }
            return send_mail(
                "UBinE Events Unsubscription Confirmation",
                body_text.render(context),
                EMAIL_SENDER,
                [self.email_address]
            )
        return False

    def generate_code(self):
        while True:
            code = get_random_string(length=Subscriber.CODE_LENGTH)
            if not Subscriber.objects.filter(code=code).exists():
                self.code = code
                return

    def save(self, *args, **kwargs):
        if not self.code:
            self.generate_code()
        super().save(*args, **kwargs)
