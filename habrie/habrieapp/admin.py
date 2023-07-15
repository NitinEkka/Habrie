from django.contrib import admin
from .models import *

# Register your models here.

class AcademicAdmin(admin.ModelAdmin):
    readonly_fields = ('enroll_id',)

admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(AcademicDetail, AcademicAdmin)
admin.site.register(Document)
