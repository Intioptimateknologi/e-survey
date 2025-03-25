from django.contrib import admin

from survey import models

admin.site.register(models.survey)
admin.site.register(models.respondent)
