from django.conf.urls import url
from . import views

app_name = "locate"

urlpatterns = [
    url(r"^$", views.index, name="index")
]
