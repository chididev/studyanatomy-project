from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.
def pelvisperineum(request):
    pelvisperineums = Pelvisperineum.objects.all()
    return render(request, 'pelvisperineum/pelvisperineum.html', {'pelvisperineums': pelvisperineums})


def pelvisperineum_detail(request, pelvisperineum_id):
    pelvisperineum_detail = get_object_or_404(
        Pelvisperineum, pk=pelvisperineum_id)
    return render(request, 'pelvisperineum/pelvisperineum_detail.html', {'pelvisperineum': pelvisperineum_detail})
