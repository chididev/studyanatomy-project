from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.
def headneck(request):
    headnecks = Headneck.objects.all()
    return render(request, 'headneck/headneck.html', {'headnecks': headnecks})


def headneck_detail(request, headneck_id):
    headneck_detail = get_object_or_404(Headneck, pk=headneck_id)
    return render(request, 'headneck/headneck_detail.html', {'headneck': headneck_detail})
