#cv_display/urls

from django.urls import path
from . import views

urlpatterns = [
    path('<str:url_name>/', views.resume, name='resume'),
    path('<str:url_name>/<str:mode>', views.resume, name='resume'),
]