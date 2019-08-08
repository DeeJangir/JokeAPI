from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.DareText)
admin.site.register(models.JokeText)
admin.site.register(models.QuotesText)
