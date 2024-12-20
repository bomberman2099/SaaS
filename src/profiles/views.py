from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()

def profile_view(request, username):
    user = request.user
    # profile_user_obj = User.objects.get(username=username)
    profile_user_obj = get_object_or_404(User, username=username)
    is_mee = user == profile_user_obj
    return HttpResponse(f"Hello {username}! - {profile_user_obj.id} - me {user.id} - {is_mee}")