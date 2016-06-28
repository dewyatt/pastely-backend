from django.contrib import admin

from . import models

admin.site.register(models.Paste)
admin.site.register(models.PasteFile)
