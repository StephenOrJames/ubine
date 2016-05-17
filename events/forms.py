from django import forms


class SubscriptionForm(forms.Form):
    email_address = forms.EmailField()
