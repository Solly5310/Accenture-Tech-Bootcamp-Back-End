from django.contrib import admin

# Register your models here.

from .models import Project, Team, User

admin.site.register(Project)
admin.site.register(Team)
admin.site.register(User)