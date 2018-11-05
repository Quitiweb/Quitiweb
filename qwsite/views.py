from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from . import models
from .forms import ContactForm

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

    def email(self):
        if self.request.method == 'GET':
            form = ContactForm
        else:
            form = ContactForm(self.request.POST)
            if form.is_valid():
                subject = form.cleaned_data['subject']
                from_email = form.cleaned_data['from_email']
                message = form.cleaned_data['message']
                try:
                    send_mail(subject, message, from_email, ['rafa@quitiweb.com'])
                except BadHeaderError:
                    return HttpResponse('Invalid header found')
                return HttpResponse('Success')
        return render(self.request, "/cv", {'form': form})