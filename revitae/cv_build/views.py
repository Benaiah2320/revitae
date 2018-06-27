#cv_build/views

from django.shortcuts import render, get_object_or_404
from .models import Resume


def resume_info(request, url_name):
