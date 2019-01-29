""" Quitiweb URL Configuration """

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Quitiweb.apps.qwsite.urls')),
    path('', include('Quitiweb.apps.qaweb.urls')),
]
