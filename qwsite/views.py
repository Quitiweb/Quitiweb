from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'qwsite/index.html')

def cv(request):
    return render(request, 'qwsite/cv.html')