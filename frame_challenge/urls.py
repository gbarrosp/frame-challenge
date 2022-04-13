from django.contrib import admin
from django.urls import path
from api import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/desafio', views.ChallengeView.as_view()),
    path('api/auth', obtain_auth_token),
]
