from django.contrib import admin

# Register your models here.
from .models import Service, Job

admin.site.register(Job)
admin.site.register(Service)
