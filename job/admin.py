from django.contrib import admin

# Register your models here.
from .models import Job,Catogery,Apply

admin.site.register(Job)
admin.site.register(Catogery)
admin.site.register(Apply)