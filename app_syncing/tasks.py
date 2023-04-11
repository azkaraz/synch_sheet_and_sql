from celery import shared_task
from app_syncing.synchronize_data import update_data


@shared_task
def update_data_from_google_sheet():
    # Получаем данные из Google Таблицы
    update_data()

