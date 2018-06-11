#cv_build/urls

from django.urls import path
from . import views

urlpatterns = [
    path('<int:resume_id>/', views.resume, name='resume')
]