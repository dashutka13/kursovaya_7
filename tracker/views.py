from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from tracker.models import Habit
from tracker.paginations import CustomPagination
from tracker.serializers import HabitSerializer
from users.permissions import IsModer, IsOwner


class HabitCreateAPIView(CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    permission_classes = (~IsModer, IsAuthenticated)

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitListAPIView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = CustomPagination


class HabitsPublicListAPIView(ListAPIView):

    serializer_class = HabitSerializer
    pagination_class = CustomPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        """Определяем параметры вывода объектов"""

        return Habit.objects.filter(is_public=True)


class HabitRetrieveAPIView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated, IsOwner | IsModer)


class HabitUpdateAPIView(UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated, IsOwner | IsModer)


class HabitDestroyAPIView(DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated, IsOwner)
