from django.contrib import admin
from .models import Project,ProjectGallery,Comment

# Register your models here.

admin.site.register(Project)
admin.site.register(ProjectGallery)
admin.site.register(Comment)

