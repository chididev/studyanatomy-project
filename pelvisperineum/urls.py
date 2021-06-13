from django.urls import path
from . import views
from pelvisperineum.views import *

urlpatterns = [
    path('pelvisperineum/', views.pelvisperineum, name='pelvisperineum'),
    path('<int:pelvisperineum_id>/', views.pelvisperineum_detail,
         name='pelvisperineum_detail'),
]
