from django.shortcuts import render
from visits.models import PageVisit


# Create your views here.


def home_page_view(request):
    page_title = "Home Page"
    path = request.path

    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=path)
    PageVisit.objects.create(path=path)

    return render(request, 'cfehome/home.html', {
        'page_title': page_title,
        'visited_count': page_qs.count(),
        'total_visits': qs.count()})


def about_page_view(request):
    page_title = "About Page"
    path = request.path
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=path)
    PageVisit.objects.create(path=path)
    return render(request, 'cfehome/about.html', {
        'page_title': page_title,
        'visited_count': page_qs.count(),
        'total_visits': qs.count()})