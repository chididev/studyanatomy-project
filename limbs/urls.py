from django.urls import path
from . import views
from limbs.views import *

urlpatterns = [
    path('limb/', views.limb, name='limb'),
    path('<int:limb_id>/', views.limb_detail, name='limb_detail'),
]
