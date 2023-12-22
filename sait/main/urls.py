from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('catalogue', views.catalogue),
    path('phone', views.phone),
    path('login', views.login),
]
