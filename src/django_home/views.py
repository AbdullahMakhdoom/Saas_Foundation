from django.http import HttpResponse
from django.shortcuts import render

def home_page_view(request, *args, **kwargs):
    page_title = {
        "page_title": "Hello World Title!"
    }
    return render(request, "home.html", page_title)
