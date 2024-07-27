from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit 


def about_view(request, *args, **kwargs):
    return home_view(request, *args, **kwargs)

def home_view(request, *args, **kwargs):

    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    try:
        percent = (page_qs.count() / qs.count()) * 100
    except:
        percent = 0

    page_title = {
        "page_title": "Hello World Title!",
        "page_visit_count": page_qs.count(),
        "percent_vist_count": percent,
        "total_visit_count": qs.count(),
    }
    PageVisit.objects.create(path=request.path)
    return render(request, "home.html", page_title)
