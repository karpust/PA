import json
import random
import sys
from datetime import datetime
import requests
from hyper.contrib import HTTP20Adapter
from avito_db import AvitoDb
from initial_data import *
from prox import proxy
import time
from my_config import token, chat_id
from initial_data import FLOORS, DISTANCE, QUERY_INTERVAL

database = AvitoDb()
id_list_db = database.get_all_id()
irrelevant_list = []
error_id_list = []


def format_msg(ad):
    publish_date = datetime.strftime(ad['time'], '%d.%m.%Y в %H:%M')
    ad_str = f"""
{ad['price']}р. {publish_date}
{str(ad['distance'])} км от м. {ad['metro']}
тел. {ad['phone']}
{ad['address']}
<a href='{ad['url']}'>перейти</a>
"""  # {ad['description']}
    # {ad['title']}
    return ad_str


def send_telegram(ad):
    text = format_msg(ad)
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {
        # 'disable_web_page_preview': True,  # убирает предпросмотр ссылки
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'HTML'
        }
    response = requests.post(url=url, data=data)
    print(response)


def get_json_data():
    """
    возвращает json -
    результаты поиска
    по заданным параметрам
    :return:
    """
    session = requests.Session()
    session.mount('https://', HTTP20Adapter())
    session.headers.update(headers)
    url = url_str
    response = session.get(url, cookies=cookies, headers=headers, params=params, proxies=proxy)
    if response.status_code != 200:
        print(f'{response.status_code}, {response.text}')
        sys.exit(1)
    result = response.json()
    # with open('rooms.json', 'w', encoding='utf-8') as file:
    #     json.dump(result, file, ensure_ascii=False)
    return result


# def get_description(ad_id):
#     ad_id = str(ad_id)
#     req = requests.Session()
#     req.mount('https://', HTTP20Adapter())
#     # https://m.avito.ru/api/18/items/2448681211?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&action=view&context=H4sIAAAAAAAA_0q0MrSqLrYytFKqULIutjI2tFIyMDMoNMhJLDQvzzIpT8w1My0wzUstNzAxNCgry8nJUrKuBQQAAP__th1jcTUAAAA
#     url = 'https://m.avito.ru/api/18/items/' + ad_id + '?key=' + key + '&action=view&context=H4sIAAAAAAAA_0q0MrSqLrYytFKqULIutjI2tFIyMDMoNMhJLDQvzzIpT8w1My0wzUstNzAxNCgry8nJUrKuBQQAAP__th1jcTUAAAA'
#     response = req.get(url, cookies=cookies, proxies=proxy)
#     if response.status_code != 200:
#         print(f'{response.status_code}, {response.text}')
#         return ''
#     else:
#         result = response.json()
#         # with open('one_room_desc.json', 'w+', encoding='utf-8') as file:
#         #     json.dump(result, file, ensure_ascii=False)
#         try:
#             return result['description']
#         except KeyError:
#             print('except KeyError', result)
#             return ''


def get_phone(ad_id):
    """
    return string phone number by ad id
    """
    # to get phone:
    # https://m.avito.ru/api/1/items/1738656219/phone?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir
    # {"status":"ok","result":{"action":{"title":"Позвонить","uri":"ru.avito://1/phone/call?number=%2B79165759646"}}}
    ad_id = str(ad_id)
    url = 'https://m.avito.ru/api/1/items/' + ad_id + '/phone?key=' + key
    req = requests.Session()
    req.mount('https://', HTTP20Adapter())
    response = req.get(url, cookies=cookies, proxies=proxy)
    if response.status_code != 200:
        print(f'{response.status_code}, {response.text}')
        return ''
    else:
        result = response.json()
        # with open('one_room.json', 'w+', encoding='utf-8') as file:
        #     json.dump(result, file, ensure_ascii=False)
        try:
            return '+' + result['result']['action']['uri'][-11:]
        except KeyError:
            print('except KeyError', result)
            return ''


def get_distance(item):
    if ', ' in item['location']:
        dist = item['location'].split(', ')[1]
        dist = dist.split(' ')
        if 'м' in dist:
            dist = int(dist[0])/1000
        else:
            dist = float(dist[0].replace(',', '.'))
    else:
        dist = 10
    return dist


def get_one_ad(item):
    ad = dict()
    ad['id'] = item['id']
    ad['total_floors'] = int(item['title'].split('/')[1].split('\xa0')[0])
    ad['distance'] = get_distance(item)
    if ad['total_floors'] > FLOORS and ad['distance'] <= DISTANCE:
        ad['title'] = item['title'].replace('\xa0', ' ')  # Комната 30 м² в 2-к., 15/17 эт.
        ad['phone'] = get_phone(ad['id'])
        timestamp = datetime.fromtimestamp(item['time'])
        ad['time'] = timestamp
        ad['price'] = int(item['price'].replace(' ', '').replace('₽вмесяц', ''))
        ad['metro'] = item['location'].split(', ')[0]
        ad['address'] = item['address']
        ad['url'] = 'https://www.avito.ru' + item['uri_mweb']
        # ad['desc'] = get_description(ad['id'])
        return ad
    else:
        return


def main():
    error_id_list = []
    database.new_room_count = 0
    data = get_json_data()
    items = data['result']['items']
    count = 0
    for item in items:
        if item['type'] == 'item':
            item = item['value']
            count += 1
            # чтобы не дергать базу проверяем список:
            if item['id'] not in id_list_db and item['id'] not in irrelevant_list:
                ad = get_one_ad(item)
                # если соответствует доп критериям, отправить сообщением:
                if ad:
                    send_telegram(ad)
                    database.update_db(**ad)
                    id_list_db.append(ad['id'])
                # если нет, отправить в список отверженных:
                else:
                    irrelevant_list.append((item['id'], 'https://www.avito.ru' + item['uri_mweb']))
                # if not ad['phone']:
                #     error_id_list.append((ad['id'], ad['url']))
                # time.sleep(5)
    # print(f'---------------------- Всего найдено {count} объявлений ----------------------------')
    # print(f'error_id_list = {error_id_list}')
    # print(f'irrelevant_list = {irrelevant_list}', end='\n')
    print(f'\nНовых объявлений: {database.new_room_count}')


if __name__ == '__main__':
    while True:
        try:
            main()
            time.sleep(QUERY_INTERVAL)
        except KeyboardInterrupt:
            print('--- parser stopped ---')
            sys.exit()









# page = 0               # Переменная для перебора страниц с объявлениями
# items = []              # Список, куда складываем объявления
# for i in range(1):
#     page += 1          # Так как страницы начинаются с 1, то сразу же итерируем
#     params['page'] = page
#     res = s.get(url_api_9, params=params)
#     # res_1 = s.get(url_api_1, params=params)
#     print(f'--------------------------------------content from api 9 = {res.content}----------------------------------------------------')
#     # print(f'--------------------------------------content from api 1 = {res_1.content}--------------------------------------------------')
#     try:
#         res = res.json()
#     except json.decoder.JSONDecodeError:
#         except_error(res)
#     if res['status'] != 'ok':
#         print(res['result'])
#         sys.exit(1)
#     if res['status'] == 'ok':
#         items_page = int(len(res['result']['items']))
#
#         if items_page > limit_page:  # проверка на "snippet"
#             items_page = items_page - 1
#
#
#         for item in res['result']['items']:
#             if item['type'] == 'item':
#                 items.append(item)
#         if items_page < limit_page:
#             cicle_stop = False
#
#
# params = {'key': key}
# for i in items:  # Теперь идем по ябъявлениям:
#     ad_id = str(i['value']['id'])
#     url_more_data_1 = 'https://m.avito.ru/api/1/rmp/show/' + ad_id
#     more_data_1 = s.get(url_more_data_1, params=params).json()  # Тут тоже много информации, можете посмотреть
#     url_more_data_2 = 'https://m.avito.ru/api/18/items/' + ad_id
#     more_data_2 = s.get(url_more_data_2, params=params).json()
#     if 'error' not in more_data_2:
#         # print(more_data_2)
#         # В more_data_2 есть всё, что надо, я вывел на принт наиболее интересные для наглядности:
#         print(more_data_2['title'])
#         print(more_data_2['price'])
#         print(more_data_2['address'])
#         url_get_phone = 'https://m.avito.ru/api/1/items/' + ad_id + '/phone'    # URL для получения телефона
#         phone = s.get(url_get_phone, params=params).json()                      # Сам запрос
#         if phone['status'] == 'ok':
#             # Прверка на наличие телефона, такой странный синтсксис, чтоб уместиться в 100 сторочек кода:
#             phone_number = requests.utils.unquote(phone['result']['action']['uri'].split('number=')[1])
#         else:
#             phone_number = phone['result']['message']
#         print(phone_number)
#         print(more_data_2['seller'])
#         # print(more_data_2['description']) # Скрыл, т.к. много букв
#         print('=======================================================\n')

