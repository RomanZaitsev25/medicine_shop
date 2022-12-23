from django.contrib import admin
from .models import Staff, Positions, Backgrounds
# Register your models here.

admin.site.register(Staff)
admin.site.register(Backgrounds)
admin.site.register(Positions)