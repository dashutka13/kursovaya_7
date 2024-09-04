from django.contrib import admin

from tracker.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "owner",
        "place",
        "time",
        "action",
        "pleasant_habit",
        "related_habit",
        "periodicity",
        "award",
        "duration",
        "is_public",
    ]
