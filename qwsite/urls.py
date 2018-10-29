from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index.as_view(), name='index'),
    path('', views.index, name='index'),
    path('cv/', views.cv, name='cv'),
]