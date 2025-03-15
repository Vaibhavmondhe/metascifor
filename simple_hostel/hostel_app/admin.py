from django.contrib import admin
from .models import Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_number', 'room_number', 'check_in_date', 'fee_status')
    list_filter = ('fee_status', 'check_in_date')
    search_fields = ('name', 'roll_number', 'room_number')
