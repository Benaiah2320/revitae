#cv_build/models.py

from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=100,
                            )
    title = models.CharField(max_length=100,
                             )
    city = models.CharField(max_length=100,
                             )
    state = models.CharField(max_length=100,
                             )
    zip = models.PositiveSmallIntegerField(verbose_name='Zip Code',
                                           )
    summary = models.TextField(help_text='One or two paragraphs summarizing your goals, history, and skills.',
                               )
    hook = models.TextField(help_text='')