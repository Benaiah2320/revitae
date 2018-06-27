import inspect
from . import models
from django.contrib import admin

for name, obj in inspect.getmembers(models):
    if inspect.isclass(obj):
        admin.site.register(obj)