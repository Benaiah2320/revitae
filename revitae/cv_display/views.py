#cv_display/views

from django.shortcuts import render, get_object_or_404
from cv_build.models import Resume


def resume(request, url_name):

    resume = get_object_or_404(Resume, url_name=url_name)

    return render(request, 'cv_display/cv.html', {'resume': resume})