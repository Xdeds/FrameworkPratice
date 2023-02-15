from django.contrib import admin
from quickstart.models import Students
# Register your models here.
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
admin.site.register(Students, StudentsAdmin)