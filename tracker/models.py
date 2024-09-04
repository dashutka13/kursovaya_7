from datetime import timedelta

from django.conf.global_settings import AUTH_USER_MODEL
from django.core.validators import MaxValueValidator
from django.db import models

from config import settings

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):

    PERIODICITY_CHOICES = [
        (1, "Каждый день"),
        (2, "Каждый будний день"),
        (3, "Каждые выходные"),
        (4, "Каждую неделю"),
    ]

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Создатель привычки",
    )

    place = models.CharField(
        max_length=100,
        verbose_name="Место",
        **NULLABLE,
        help_text="Укажите место выполнения.",
    )

    time = models.TimeField(
        verbose_name="Время", **NULLABLE, help_text="Укажите время выполнения."
    )

    action = models.CharField(
        max_length=100,
        verbose_name="Действие",
        **NULLABLE,
        help_text="Укажите действие, которое необходимо выполнить.",
    )

    pleasant_habit = models.BooleanField(
        default=False,
        verbose_name="Приятная привычка",
        help_text="Отметьте, если привычка приятная.",
    )

    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Связанная привычка",
        help_text="Привычка, которая связана с другой привычкой",
    )

    periodicity = models.PositiveIntegerField(
        default=1,
        choices=PERIODICITY_CHOICES,
        verbose_name="Периодичность",
        **NULLABLE,
        help_text="Выберите периодичность выполнения.",
    )

    award = models.CharField(
        max_length=100,
        **NULLABLE,
        verbose_name="Вознаграждение ",
        help_text="Укажите вознаграждение.",
    )

    duration = models.DurationField(
        verbose_name="Время на выполнение (сек)",
        help_text="Укажите время, за которое необходимо выполнить действие.",
        **NULLABLE,
        validators=[MaxValueValidator(timedelta(seconds=120))],
    )

    is_public = models.BooleanField(
        default=False, verbose_name="Признак публичности", help_text="Доступно всем."
    )

    def __str__(self):
        return f"Я буду {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
        ordering = ("pk",)
