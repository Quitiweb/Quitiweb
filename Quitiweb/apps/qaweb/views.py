from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render

from . import models
from . import map

# Create your views here.
def mapa(request):
    map.generate_map()

    return render(request, 'qaweb/map.html')

def index(request):
    return render(request, 'qaweb/practice.html')

#class index(ListView):
#    model = models.Map
#    template_name = 'practice.html'
#    context_object_name = 'practice_list'
#    
#    def head(self):
#        mapa = self.get_queryset().objects.all()
#        response = HttpResponse('')
#        response['Last_Modified'] = mapa
#        return response