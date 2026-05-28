from django.contrib import admin
from .models import doctor


@admin.register(doctor)
class DoctorAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'specialization',
        'experience',
        'city',
        'email',
        'phone',
        'hospital',
        'available_time'
    )

    search_fields = (
        'name',
        'specialization',
        'city',
        'hospital'
    )

    list_filter = (
        'specialization',
        'city'
    )

    ordering = ('name',)