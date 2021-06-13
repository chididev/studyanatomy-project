from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.
@login_required
def neuroanatomy(request):
    neuroanatomys = Neuroanatomy.objects.all()
    return render(request, 'neuroanatomy/neuroanatomy.html', {'neuroanatomys': neuroanatomys})


@login_required
def neuroanatomy_detail(request, neuroanatomy_id):
    neuroanatomy_detail = get_object_or_404(Neuroanatomy, pk=neuroanatomy_id)
    return render(request, 'neuroanatomy/neuroanatomy_detail.html', {'neuroanatomy': neuroanatomy_detail})
