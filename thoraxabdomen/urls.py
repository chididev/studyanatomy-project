from django.urls import path
from . import views
from thoraxabdomen.views import *

urlpatterns = [
    path('thoraxabdomen/', views.thoraxabdomen, name='thoraxabdomen'),
    path('<int:thoraxabdomen_id>/', views.thoraxabdomen_detail,
         name='thoraxabdomen_detail'),
]
