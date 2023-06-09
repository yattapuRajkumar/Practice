from django.urls import path
from .views import *

urlpatterns=[
    path('',lead_list,name='lead-list'),
    path('<int:pk>/',lead_detail,name='lead-detail'),
    path('<int:pk>/update/',lead_update,name='lead-update'),
    path('<int:pk>/delete/',lead_delete,name='lead-delete'),
    path('create-a-new/',lead_create,name='lead-create')
]