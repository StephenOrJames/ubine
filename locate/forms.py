from django import forms


class SearchForm(forms.Form):
    QUADRANGLES = (
        ("fargo", "Fargo"),
        ("porter", "Porter"),
        ("red_jacket", "Red Jacket"),
        ("richmond", "Richmond"),
        ("wilkeson", "Wilkeson"),
    )
    quadrangle = forms.ChoiceField(widget=forms.Select, choices=QUADRANGLES)
    room = forms.IntegerField(max_value=1000, min_value=0, widget=forms.TextInput)
