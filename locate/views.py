from django.shortcuts import render
from locate.forms import SearchForm
from locate.rooms import get_building


def index(request):
    form = SearchForm(request.GET)
    if request.GET.get("quadrangle") and request.GET.get("room"):
        if form.is_valid():
            quadrangle = form.cleaned_data["quadrangle"]
            room = form.cleaned_data["room"]
            building = get_building(quadrangle, room)
            return render(request, "locate/locate.html", {
                "form": form,
                "quadrangles": SearchForm.QUADRANGLES,
                "quadrangle": quadrangle,
                "quadrangle_name": quadrangle.replace("_", " ").title(),
                "room": room,
                "building": building,
                "floor": room // 100,
            })
    return render(request, "locate/locate.html", {
        "form": form,
        "quadrangles": SearchForm.QUADRANGLES,
    })
