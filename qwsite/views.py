from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from . import models

def index(request):
    return render(request, 'qwsite/index.html')

class cv(ListView):
    model = models.cv
    template_name = 'cv.html'
    context_object_name = 'cv_list'
    
    def head(self):
        cv = self.get_queryset().objects.all()
        response = HttpResponse('')
        response['Last_Modified'] = cv
        return response