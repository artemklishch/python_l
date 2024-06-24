from django.contrib import admin
# from . import models
from .models import Course, Category

admin.site.site_header = "Courses Admin"
admin.site.site_title = "My Courses"
admin.site.index_title = "Welcome to the Courses admin area"


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category')


class CoursesInline(admin.TabularInline):
    model = Course
    extra = 1
    exclude = ['created_at']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Dates', {'fields': ['created_at'], 'classes': ['collapse']})
    ] # what fields will be displayed in single table with courses
    inlines = [CoursesInline] # connect to single table with courses


# admin.site.register(models.Category, CategoryAdmin)
# admin.site.register(models.Course, CourseAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
