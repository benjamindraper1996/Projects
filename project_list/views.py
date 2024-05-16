from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base/index.html')

def html(request):
    return render(request, 'base/html.html')

def css(request):
    return render(request, 'base/css.html')

def javascript(request):
    return render(request, 'base/javascript.html')

def python(request):
    return render(request, 'base/python.html')
