#cv_build/urls

from django.urls import path
from . import views

urlpatterns = [
    path('<str:url_name>/header', views.resume_header_input, name='resume_header_input')
]