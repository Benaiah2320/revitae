#cv_build/urls

from django.urls import path
from . import views

urlpatterns = [
    path('<str:url_name>/', views.resume, name='resume')
]