from django.urls import path
from . import views
from neuroanatomy.views import *

urlpatterns = [
    path('neuroanatomy/', views.neuroanatomy, name='neuroanatomy'),
    path('<int:neuroanatomy_id>/', views.neuroanatomy_detail,
         name='neuroanatomy_detail'),
]
