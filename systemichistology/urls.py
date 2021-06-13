from django.urls import path
from . import views
from histology.views import *

urlpatterns = [
    path('systemic/', views.systemic, name='systemic_histology'),
    path('<int:systemic_id>/', views.systemic_detail, name='systemic_detail'),
]
