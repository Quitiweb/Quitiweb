from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cv', views.cv, name='cv'),
    path('success', views.successView, name='success'),
    #path('cv', views.cv.as_view(), name='cv'),
]