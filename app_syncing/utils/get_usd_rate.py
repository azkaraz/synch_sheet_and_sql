import json
import requests
import xmltodict


def get_uds_rate() -> float:

    # Получаем текущий курс доллара
    url = 'https://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    xml = response.content.decode('windows-1251')
    data = json.loads(json.dumps(xmltodict.parse(xml)))
    usd_rate = float(data['ValCurs']['Valute'][13]['Value'].replace(',', '.'))

    return usd_rate
