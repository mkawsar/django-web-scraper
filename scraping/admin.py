from django.contrib import admin
from scraping.models import Job


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'url', 'createdAt')


# Register your models here.
admin.site.register(Job, JobAdmin)
