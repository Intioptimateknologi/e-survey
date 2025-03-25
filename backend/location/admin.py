from django.contrib import admin

from location import models

admin.site.register(models.desa)
admin.site.register(models.kecamatan)
admin.site.register(models.kabupaten)
admin.site.register(models.provinsi)

