#cv_build/views

from django.shortcuts import render, get_object_or_404
from .models import Resume

def resume(request, resume_id):

    resume = get_object_or_404(Resume, pk=resume_id)

    return render(request, 'cv_build/cv.html', {'resume': resume})
