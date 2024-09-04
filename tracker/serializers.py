from rest_framework import serializers

from tracker.models import Habit
from tracker.validators import RelatedHabitValidator, RewardValidator


class HabitSerializer(serializers.ModelSerializer):
    """Сериализотор для модели привычки"""

    class Meta:
        model = Habit
        fields = "__all__"
        read_only_fields = ["user"]
        validators = [
            RewardValidator(field="reward"),
            RelatedHabitValidator(field="related_habit"),
        ]
