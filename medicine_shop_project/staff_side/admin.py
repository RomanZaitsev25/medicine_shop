from django.contrib import admin

from .forms import StaffForm
from .models import Staff, Positions, Backgrounds
# Register your models here.


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'date_of_birth', 'position')
    list_filter = ('second_name', 'date_of_birth', 'position', 'schedule_type')
    search_fields = ('first_name', 'second_name', 'date_of_birth', 'position')
    form = StaffForm


@admin.register(Positions)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('post_name', 'responsibility')
    list_filter = ('post_name', 'responsibility')
    search_fields = ('post_name', 'responsibility')


@admin.register(Backgrounds)
class BackgroundAdmin(admin.ModelAdmin):
    list_display = ('educational_institution', 'education_completeness')
    list_filter = ('educational_institution',)
    search_fields = ('educational_institution', 'education_completeness')
