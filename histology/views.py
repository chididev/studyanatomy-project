from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.
def tissue(request):
    tissues = Tissue.objects.all()
    return render(request, 'histology/tissue.html', {'tissues': tissues})


def tissue_detail(request, tissue_id):
    tissue_detail = get_object_or_404(Tissue, pk=tissue_id)
    return render(request, 'histology/tissue_detail.html', {'tissue': tissue_detail})
