from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.
def thoraxabdomen(request):
    thoraxabdomens = Thoraxabdomen.objects.all()
    return render(request, 'thoraxabdomen/thoraxabdomen.html', {'thoraxabdomens': thoraxabdomens})


def thoraxabdomen_detail(request, thoraxabdomen_id):
    thoraxabdomen_detail = get_object_or_404(
        Thoraxabdomen, pk=thoraxabdomen_id)
    return render(request, 'thoraxabdomen/thoraxabdomen_detail.html', {'thoraxabdomen': thoraxabdomen_detail})
