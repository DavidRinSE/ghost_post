from django.urls import path
from ghost_post import views

urlpatterns = [
    path('', views.index),
]