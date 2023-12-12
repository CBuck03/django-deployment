from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Topic)
admin.site.register(models.Webpage)
admin.site.register(models.AccessRecord)
admin.site.register(models.Users)
admin.site.register(models.UserProfileInfo)
