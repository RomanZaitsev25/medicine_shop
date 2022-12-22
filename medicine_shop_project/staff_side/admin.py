from django.contrib import admin
from .models import Staff, Positions
# Register your models here.

admin.site.register(Staff, Positions)
