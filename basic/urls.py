from django.urls import path
from . import views
from basic.views import *

urlpatterns = [
    path('basic/', views.basic, name='basic'),
    path('<int:basic_id>/', views.basic_detail, name='basic_detail'),
]
