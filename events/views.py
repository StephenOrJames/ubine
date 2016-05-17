from datetime import datetime

from django.http.response import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from events.forms import SubscriptionForm
from events.models import Event, Subscriber


def index(request):
    events = Event.objects.all()

    if request.GET.get("id"):
        events = events.filter(id=request.GET["id"])
    if request.GET.get("title"):
        events = events.filter(title__contains=request.GET["title"])
    if request.GET.get("after"):
        try:
            date_after = datetime.strptime(request.GET["after"], "%Y-%m-%d")
        except ValueError:
            pass
        else:
            date_after = timezone.make_aware(date_after, timezone.get_current_timezone())
            events = events.filter(start_time__gte=date_after)
    if request.GET.get("before"):
        try:
            date_before = datetime.strptime(request.GET["before"], "%Y-%m-%d")
        except ValueError:
            pass
        else:
            date_before = timezone.make_aware(date_before, timezone.get_current_timezone())
            events = events.filter(end_time__lt=date_before)

    return render(request, "events/events.html", {
        "events": events,
        "query": request.GET
    })


def subscribe(request, code=None):
    if code:
        subscriber = Subscriber.objects.filter(code=code).first()
        if subscriber and subscriber.opt_in():
            return HttpResponse("Confirmation successful")
        return HttpResponse("Confirmation unsuccessful")
    else:
        if request.method == "POST":
            form = SubscriptionForm(request.POST)
            if form.is_valid():
                Subscriber.create(form.cleaned_data["email_address"])
                return HttpResponse("Valid")
            else:
                return HttpResponse("Invalid")
        else:
            form = SubscriptionForm()
            return render(request, "events/subscribe.html", {
                "form": form
            })


def unsubscribe(request, code):
    subscriber = Subscriber.objects.filter(code=code).first()
    if subscriber:
        if subscriber.opt_out():
            return HttpResponse("Unsubscribed successfully")
        else:
            return HttpResponse("Unsubscribe failure, but good code")
    else:
        return HttpResponse("Invalid code")
