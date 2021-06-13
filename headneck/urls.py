from django.urls import path
from . import views
from headneck.views import *

urlpatterns = [
    path('headneck/', views.headneck, name='headneck'),
    path('<int:headneck_id>/', views.headneck_detail,
         name='headneck_detail'),
]
