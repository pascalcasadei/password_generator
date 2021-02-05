from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, "generator/home.html")


def about(request):
    return render(request, "generator/about.html")


def password(request):
    thepassword = "testing"
    characters = list("abcdefghijklmnopqrstuvwxyz")
    if request.GET.get("uppercase"):
        characters.extend(list("ABCDEFGHIJKLNMOPQRSTUVWXYZ"))

    if request.GET.get("numbers"):
        characters.extend(list("1234567890"))

    if request.GET.get("Special"):
        characters.extend(list("@#[]!\"£$%&/()=?^"))

    lunghezza = int(request.GET.get("length", 14))
    thepassword = ""
    for x in range(lunghezza):
        thepassword += random.choice(characters)
    return render(request, "generator/password.html",
                  {"password": thepassword})
