from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('about/', views.about_page_view, name='about'),
    path('protected/', views.pw_protected_view, name='protected'),
    path('protected/user_only/', views.user_only, name='user_only'),
    path('protected/staff_only/', views.staff_only, name='staff_only'),

]