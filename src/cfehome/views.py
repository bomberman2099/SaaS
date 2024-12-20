from django.shortcuts import render
from visits.models import PageVisit
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
# Create your views here.

login_url = settings.LOGIN_URL
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


valid_code = 'abc'
def pw_protected_view(request):
    is_allowed = request.session.get('protected_page_allowed') or None
    print(is_allowed, type(is_allowed))
    if request.method == "POST":
        user_pw_send = request.POST['code'] or None
        if user_pw_send == valid_code:
            is_allowed = 1
            request.session['protected_page_allowed'] = is_allowed

    if is_allowed:
        return render(request, 'protected/view.html', {})
    return render(request, 'protected/entry.html', {})


@login_required(login_url=login_url)
def user_only(request):
    return render(request, 'protected/user_only.html', {})


@staff_member_required(login_url=login_url)
def staff_only(request):
    return render(request, 'protected/user_only.html', {})
