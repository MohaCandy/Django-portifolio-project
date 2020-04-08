from django.contrib import admin

from .models import Informations, Languages, Projects

# Register your models here.
admin.site.register(Informations)
admin.site.register(Projects)
admin.site.register(Languages)