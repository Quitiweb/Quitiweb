from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from Quitiweb.apps.qwsite.models import cv
from .forms import ContactForm


def index(request):
    curriculo = cv.objects.all().first()
    template = loader.get_template('qwsite/index.html')

    context = {'cv': curriculo}

    return HttpResponse(template.render(context, request))


def curriculum_vitae(request):
    cv_list = cv.objects.all()
    template = loader.get_template('qwsite/cv.html')
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['rafa@quitiweb.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found')

            return redirect('success')
        else:
            print('Error en el formulario')

    context = {
        'cv_list': cv_list,
        'form': form,
    }

    return HttpResponse(template.render(context, request))


def success_view(request):
    return render(request, 'qwsite/success.html')
