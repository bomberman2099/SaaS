from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_list_view, name='profile_list_view'),
    path('<str:username>/', views.profile_details_view, name='profile_details_view'),

]