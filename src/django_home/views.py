from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit 

def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)

    page_title = {
        "page_title": "Hello World Title!",
        "page_visit_count": page_qs.count(),
        "percent_vist_count": (page_qs.count() / qs.count()) * 100,
        "total_visit_count": qs.count(),
    }
    PageVisit.objects.create(path=request.path)
    return render(request, "home.html", page_title)
