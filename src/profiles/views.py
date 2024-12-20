from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()

def profile_list_view(request):
    context = {
        "object_list": User.objects.filter(is_active=True),
    }
    return render(request, "profile/list.html", context)


def profile_details_view(request, username):
    user = request.user
    print(user.has_perm("auth.view_user"))
    print(user.has_perm("visits.view_pagevisit"))
    # profile_user_obj = User.objects.get(username=username)
    profile_user_obj = get_object_or_404(User, username=username)
    context = {
        "object": profile_user_obj,
        'instance': profile_user_obj,
        'is_me': profile_user_obj == user,
    }
    return render(request, "profile/detail.html", context)
