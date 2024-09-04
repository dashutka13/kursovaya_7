from rest_framework import serializers


class RewardValidator:
    """
    - Исключает одновременный выбор связанной привычки и указания вознаграждения.
    - Исключает указание вознаграждения для приятной привычки.
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reward = value.get(self.field)
        related_habit = value.get("related_habit")
        is_nice = value.get("is_nice")
        if reward and is_nice:
            raise serializers.ValidationError(
                "У приятной привычки не может быть вознаграждения."
            )
        elif reward and related_habit:
            raise serializers.ValidationError(
                "Нельзя одновременно заполнить и поле вознаграждения, и поле связанной привычки."
            )


class RelatedHabitValidator:
    """
    - Исключает попадание в связанные привычки привычки без признака приятной привычки.
    - Исключает указание связанной привычки для приятной привычки.
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        related_habit = value.get(self.field)
        pleasant_habit = value.get("pleasant_habit")
        if related_habit and not related_habit.pleasant_habit:
            raise serializers.ValidationError(
                "В связанные привычки могут попадать только привычки с признаком приятной привычки."
            )
        if related_habit and pleasant_habit:
            raise serializers.ValidationError(
                "У приятной привычки не может быть связанной привычки."
            )
