from django.conf.urls import url
from . import views

app_name = "events"

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^subscribe/(?:(?P<code>[a-zA-Z0-9]+)/)?$", views.subscribe, name="subscribe"),
    url(r"^unsubscribe/(?P<code>[a-zA-Z0-9]+)/$", views.unsubscribe, name="unsubscribe"),
]
