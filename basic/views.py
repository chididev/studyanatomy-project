from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.
@login_required
def basic(request):
    basics = Basic.objects.all()
    return render(request, 'basic/basic.html', {'basics': basics})


@login_required
def basic_detail(request, basic_id):
    basic_detail = get_object_or_404(Basic, pk=basic_id)
    return render(request, 'basic/basic_detail.html', {'basic': basic_detail})
