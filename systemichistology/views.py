from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.

@login_required
def systemic(request):
    systemics = Systemic.objects.all()
    return render(request, 'systemichistology/systemic.html', {'systemics': systemics})


@login_required
def systemic_detail(request, systemic_id):
    systemic_detail = get_object_or_404(Systemic, pk=systemic_id)
    return render(request, 'systemichistology/systemic_detail.html', {'systemic': systemic_detail})
