import requests
from hyper.contrib import HTTP20Adapter
from selectolax.parser import HTMLParser
from initial_data import cookies, headers
from urllib.parse import unquote
import json

# не актуально, всю эту инфу можно получить через браузер - networks
def get_json_data(url):
    """
    ф-ция для определения ключей
    по значениям которых будет проходить поиск
    создает json файл
    """
    session = requests.Session()
    session.mount('https://', HTTP20Adapter())
    if cookies:
        headers['cookie'] = cookies
    session.headers.update(headers)
    response = session.get(url)
    html = response.text
    tree = HTMLParser(html)
    scripts = tree.css('script')
    for script in scripts:
        if 'window.__initialData__' in script.text():
            string_json = script.text().split(';')[0].split('=')[-1].strip()
            # unquote заменяет %7B%22 на пробелы, убрали кавычки:
            string_json = unquote(string_json)[1:-1]
            # преобразуем строку в json:
            data = json.loads(string_json)

            with open('data.json', 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False)


def main():
    # комнаты списком:
    # url = 'https://m.avito.ru/moskva/komnaty/sdam/na_dlitelnyy_srok-ASgBAgICAkSQA74QqAn2YA?f=ASgBAQECA0SQA74QqAn2YPbiDqzx2wIDQOQWFOT8AcK~DRTAyjX44g4UsPHbAgJF_AcVeyJmcm9tIjoxOCwidG8iOm51bGx9xpoMFXsiZnJvbSI6MCwidG8iOjIwMDAwfQ&user=1'
    # url = 'https://m.avito.ru/moskva/komnaty/sdam/na_dlitelnyy_srok-ASgBAgICAkSQA74QqAn2YA?f=ASgBAgECB0SQA74QgAjyUqgJ9mDkFgLCvg0C9uIOrPHbAvjiDrDx2wICRfwHFXsiZnJvbSI6MTgsInRvIjpudWxsfcaaDBl7ImZyb20iOjE1MDAwLCJ0byI6MjAwMDB9&localPriority=1&radius=0&user=1&presentationType=serp'
    # одна комната, балкон в описании:
    # url = 'https://m.avito.ru/moskva/komnaty/komnata_20m_v_4-k._612et._1853413766'
    # одна комната балкон в поле:
    url = 'https://m.avito.ru/moskva/kvartiry/1-k._kvartira_377m_39et._2429897348'
    get_json_data(url)


if __name__ == '__main__':
    main()

