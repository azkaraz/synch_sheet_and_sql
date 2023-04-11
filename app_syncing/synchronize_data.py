import os

from app_syncing.models import SheetData
from app_syncing.service import connect_to_google
from app_syncing.utils.get_usd_rate import get_uds_rate

import logging
from googleapiclient.discovery import build
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SPREADSHEET_ID = os.environ.get('SPREADSHEET_ID')
RANGE_NAME = 'Лист1!A2:D'


def synchronize_data():
    """ Скачивает всю таблицу и обновляет БД """

    # Устанавливаем соединение с таблицей
    service = build('sheets', 'v4', credentials=connect_to_google())
    sheet = service.spreadsheets()

    # Получаем данные из таблицы
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', [])

    # Получаем актуальный курс USD по ЦБ РФ
    usd_rate = get_uds_rate()

    # Распаковываем данные и записываем в БД
    for row in values:
        number = row[0]
        order_number = row[1]
        cost_usd = float(row[2])
        delivery_date = datetime.strptime(row[3], '%d.%m.%Y').date()
        cost_rub = cost_usd * usd_rate

        data_pack = {'number': number, 'order_number': order_number, 'cost_usd': cost_usd,
                     'delivery_date': delivery_date, 'cost_rub': cost_rub}

        sheet_data, created = SheetData.objects.update_or_create(number=number,
                                                                 defaults=data_pack)
        if not created:
            continue
        sheet_data.save()

    logging.warning('Synchronization was successful')
    return
