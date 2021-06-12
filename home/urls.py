from django.urls import path
from . import views
from home.views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('gross/', views.gross, name='gross'),
    path('histo/', views.histo, name='histo'),
    path('embryo/', views.embryo, name='embryo'),
]
