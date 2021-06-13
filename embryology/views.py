from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.
def embryology(request):
    embryologys = Embryology.objects.all()
    return render(request, 'embryology/embryology.html', {'embryologys': embryologys})


def embryology_detail(request, embryology_id):
    embryology_detail = get_object_or_404(Embryology, pk=embryology_id)
    return render(request, 'embryology/embryology_detail.html', {'embryology': embryology_detail})
