from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Contact)
admin.site.register(Blog)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Fields to display in the admin list view
    search_fields = ('title',)  # Enable search by project title

admin.site.register(Project, ProjectAdmin)
