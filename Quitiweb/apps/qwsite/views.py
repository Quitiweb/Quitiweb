from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from . import models
from .forms import ContactForm

def index(request):
    return render(request, 'qwsite/index.html')

def cv(request):
    cv_list = models.cv.objects.all()
    template = loader.get_template('qwsite/cv.html')

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['rafa@quitiweb.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found')

            form = ContactForm()
            return redirect('success')
        else:
            print('Error en el formulario')

    context = {
        'cv_list': cv_list,
        'form': form,
    }

    return HttpResponse(template.render(context, request))

def successView(request):
    return render(request, 'qwsite/success.html')