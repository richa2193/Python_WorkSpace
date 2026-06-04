from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    """Admin interface for the :class:`Doctor` model.

    * ``list_display`` shows key columns in the list view.
    * ``search_fields`` enables quick search on name and specialty.
    * ``list_filter`` adds filtering by specialty and experience.
    """

    list_display = ("name", "specialty", "contact", "email", "experience_years", "consultation_fee", "created_at")
    search_fields = ("name", "specialty", "email")
    list_filter = ("specialty", "experience_years")
    ordering = ("-created_at",)
