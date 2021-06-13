from django.urls import path
from . import views
from histology.views import *

urlpatterns = [
    path('tissue/', views.tissue, name='tissue_histology'),
    path('<int:tissue_id>/', views.tissue_detail, name='tissue_detail'),
]
