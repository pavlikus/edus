from django.contrib import admin

from .models import Course, CourseStream, Schedule

from sorl.thumbnail.admin import AdminImageMixin


class ScheduleInline(admin.TabularInline):
    
    model = Schedule
    extra = 0


@admin.register(Course)
class CourseAdmin(AdminImageMixin, admin.ModelAdmin):
    
    prepopulated_fields = {"slug": ("name",)}


@admin.register(CourseStream)
class CourseStreamAdmin(admin.ModelAdmin):

    list_display = 'name', 'date_start', 'date_end'
    inlines = [ScheduleInline]
    
    # prepopulated_fields = {"slug": ("name",)}


admin.site.register(Schedule)
