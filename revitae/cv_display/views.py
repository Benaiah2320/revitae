#cv_display/views

from django.shortcuts import render, get_object_or_404
from cv_build.models import Resume


def resume(request, url_name, mode=''):

    resume = get_object_or_404(Resume, url_name=url_name)

    if mode == 'print':
        template = 'cv_display/cv_print.html'

    else:
        template = 'cv_display/cv.html'

    return render(request, template, {'resume': resume})