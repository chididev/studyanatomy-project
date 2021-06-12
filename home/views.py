from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home/homepage.html')


def gross(request):
    return render(request, 'home/gross.html')


def histo(request):
    return render(request, 'home/histo.html')


def embryo(request):
    return render(request, 'home/embryo.html')
