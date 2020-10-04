from django.contrib import admin

from .models import Teacher, Student

from sorl.thumbnail.admin import AdminImageMixin


@admin.register(Teacher)
class TeacherAdmin(AdminImageMixin, admin.ModelAdmin):
    
    prepopulated_fields = {"slug": ("first_name", "last_name")}


admin.site.register(Student)
