from django.urls import path
from bdd_django_app import views

urlpatterns = [
    path('users/', views.users, name='get_users')
]
