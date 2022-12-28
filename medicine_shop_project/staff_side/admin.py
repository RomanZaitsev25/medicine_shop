from django.contrib import admin

from .forms import StaffForm
from .models import Staff, Positions, Backgrounds
# Register your models here.


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'date_of_birth', 'position')
    list_display_links = ('first_name',)
    list_filter = ('second_name', 'date_of_birth', 'position', 'schedule_type')
    search_fields = ('first_name', 'second_name', 'date_of_birth', 'position')
    fieldsets = (
        ('Общие данные', {
            'classes': ('collapse',),
            'fields': ('first_name', 'second_name', 'female', 'date_of_birth')
        }),
        ('Профессиональные данные', {
            'classes': ('collapse',),
            'fields': ('schedule_type', 'background', 'position',
                       '_salary', 'vacations')
        }),
    )

    form = StaffForm
    save_on_top = True


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


admin.site.site_title = 'Админ панель сайта о заказе лекарств'
admin.site.site_header = 'Админ панель сайта о заказе лекарств'