from django.contrib import admin
from .models import Students

@admin.register(Students)
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'roll', 'city']
