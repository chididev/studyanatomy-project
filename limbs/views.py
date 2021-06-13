from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.
def limb(request):
    limbs = Limb.objects.all()
    return render(request, 'limbs/limbs.html', {'limbs': limbs})


def limb_detail(request, limb_id):
    limb_detail = get_object_or_404(Limb, pk=limb_id)
    return render(request, 'limbs/limbs_detail.html', {'limb': limb_detail})
