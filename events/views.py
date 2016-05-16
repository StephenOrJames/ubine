from datetime import datetime

from django.shortcuts import render
from django.utils import timezone
from events.models import Event


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
