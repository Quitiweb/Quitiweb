from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cv', views.curriculum_vitae, name='cv'),
    path('success', views.success_view, name='success'),
]
