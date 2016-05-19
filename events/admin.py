from django import forms
from django.contrib import admin
from pagedown.widgets import AdminPagedownWidget
from events.models import Event


class EventsForm(forms.ModelForm):
    description = forms.CharField(widget=AdminPagedownWidget())


class EventsAdmin(admin.ModelAdmin):
    form = EventsForm


admin.site.register(Event, EventsAdmin)
