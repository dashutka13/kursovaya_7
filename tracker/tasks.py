from celery import shared_task
from tracker.models import Habit
from tracker.services import send_tg_message


@shared_task
def remind_of_habit():
    """
    Напоминание о выполнении привычки
    """
    habits = Habit.objects.all()
    for habit in habits:
        if habit.owner.tg_chat_id:
            message = f"""Привет!\nНе забудь сегодня выполнить привычку: "{habit.action}"\n 
                Время: {habit.time.strftime("%H:%M")}\n
                Место: {habit.place}"""

            send_tg_message(message, habit.owner.tg_chat_id)
