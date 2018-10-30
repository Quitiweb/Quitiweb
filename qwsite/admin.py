from django.contrib import admin

from . import models

admin.site.register(models.Hobbies)
admin.site.register(models.Education)
admin.site.register(models.Experience)
admin.site.register(models.Skills)
admin.site.register(models.cv)