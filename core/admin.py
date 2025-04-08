from django.contrib import admin
from .models import Course, Evaluation
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title'
    ]
    list_display_links = [
        'id',
        'title'
    ]
    ordering = ['-id']
    
@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'course',
        'email',
        'evaluation',
    ]
    list_display_links = [
        'name',
        'course',
    ]
    ordering = ['-id']