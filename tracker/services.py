from config.settings import TELEGRAM_TOKEN, TELEGRAM_URL
import requests


def send_tg_message(message, chat_id):
    """Отправка сообщения в Telegram"""
    params = {"text": message, "chat_id": chat_id}
    try:
        response = requests.get(
            f"{TELEGRAM_URL}{TELEGRAM_TOKEN}/sendMessage", params=params
        )
        response.raise_for_status()
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
