from django.contrib import admin
from models import Devotion


class DevotionAdmin(admin.ModelAdmin):
    list_display = ('date', 'title')

admin.site.register(Devotion, DevotionAdmin)
