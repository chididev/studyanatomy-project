from django.urls import path
from . import views
from embryology.views import *

urlpatterns = [
    path('embryology/', views.embryology, name='embryology'),
    path('<int:embryology_id>/', views.embryology_detail, name='embryology_detail'),
]
