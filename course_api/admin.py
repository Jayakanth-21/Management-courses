from django.contrib import admin
from .models import Student,CourseMaster,Enrollment
# Register your models here.

admin.site.register(Student)
admin.site.register(CourseMaster)
admin.site.register(Enrollment)
