"""get url, cookies, headers from curlconverter"""

url_str = 'https://m.avito.ru/api/11/items?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&categoryId=23&params\\[200\\]=1055&params\\[121019\\]=2849878&params\\[121020\\]=2849880&locationId=637640&localPriority=1&footWalkingMetro=0&params\\[596\\]=6203&priceMin=15000&priceMax=20000&params\\[510-from-int\\]=18&params\\[512\\]=5305&params\\[110497\\]=1&params\\[1458\\]=1&owner\\[\\]=private&sort=date&withImagesOnly=1&isGeoProps=true&page=1&lastStamp=1655482800&display=list&limit=30'

cookies = {
    'u': '2tciqu1q.qe5y8h.fwquxt59heg0',
    '_ym_d': '1655027494',
    '_ym_uid': '165502749412228827',
    '_gcl_au': '1.1.366694497.1655027494',
    'tmr_lvidTS': '1655027494729',
    'tmr_lvid': '602d1e9fe65a87c9f458933b1e1f76d0',
    'adrcid': 'AdVZ9AZcyhSLX0PRJo_fDag',
    'uxs_uid': '04d9a9f0-ea36-11ec-82d1-a96559ad0bb1',
    'buyer_laas_location': '637640',
    'abp': '0',
    'buyer_location_id': '637640',
    '_gid': 'GA1.2.1527182154.1655369357',
    '_ym_isad': '2',
    'isCriteoSetNew': 'true',
    'st': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoidko0TkJ5SlU2TElJTGRDY3VNTkdBZm5PRWwySzdtS01KZXBFMDh1VUFISmJCTzdXeTdabjByWm5uVERhZHl5YVdUU0JDNkhibUszazZ5VnEyYWlnbTQralBzZFNrcGYrWFFYZmxPZ1doMXFzM1BQc0dOWUZQUllUeUFheCtJbktHdWhqQk0vbklVdlFyUllDdnZnaU5FdzlVbXVQRkxSV0ZoUTVvL0Q2ZkdRS2RyMzV2V04yUnY2SWFiU3U0L3VNT3RHbklXWnFsZkh4SDFYVWpmSUN2ZElFeEdySDJRM2VCY1BxellmNTBZRWU2ZWVzc2RjY0ppNm1aaUFKQjVJcE9hOEFSNFVPZHlrTThuajhGRHJUd2xzZ3pDRkNxUm9OYzFKVmRXOFVnYnJhOUNxOEZrUkhjWkpNYWtLcmUwMVhIc05YZENoN2ZxSDl3Rk9MZkxoT0RDbk1OL20yUzhYamppR0s2QmlHaUdQUFlwUStOT0RTWjg2c1V1NjhxcUhnZktrY3VaSkI3dHMzcWdrTXlxVDJoVFMwdlBwbWEwczhlSHBpcUVIaU1jL0U2bVVWQWhXQjkzNkFzTGhPSzNtRWMrdmx2OFRLMkVYYUJOU084djFESm1OcFpBbGFpbXRrOEs2UUo0QnRCMGpCK1lIN1ZzaENzUlhHMk1IZGk0RXBpblNma21iT1Jvb2FOazhBK1NRRUV6YjVTMG1QeGZNeGZ0cFlteFFjbFdVcWhXQmN3RkVWbk5hZEIvc1M0TWk0L0pzZ0lnSlBXaElnNWdOSVUvS3lnVzRueTlWcE95cXNuSmxUSitPTks2eVQwejFGMnVBSmt2cm5XREhvZ2RhZ2RpRHBwVUwzaDNyOU9uL0E3VldYeXFLeHc4bGxBRlp1cWFuSkE0d1A5bGxWSHUxUGptai9JTWZFcDc5dzhQTGVEQ2F6VGp0M3VCVlZDd2E5d2syM3VlRFJHdVJTOXUxTHY5TXhzc01CMnVHYVVHeHNaRHJwNDJrdkN2WndMTWM2L21RaVpKeDRVdlpicXoxaVh2NTlCM3pDN0RYZ2luOCtyWXl1a0liNlljMTdhcGZkTFpjc2UxUGo5T3FnQnVFeng2Rlo0QTF6ckt0VjZqZEcyaHdpcWdqQ1NQN3JsK1p3Y0tBelVvc2hhTElZYnVwWFROc2NlemNpL011T1UydnpiSWZNeTcyS1ZZY29IZHYvT1VlM3J4TVBIZURPNDQ5cldVVnhHVi9GcUlXVmE5c3JjV01ibVZVVGRIbVpBQnBrZlorR3g5dTdjK3l4bFpBRklSMXA0d3c0Zy9RL2hvZlFYR2FmMGJIZGhoMFJLV1lMbzlMNk5KVFRtY0JJMm1jbExOV01keUNyUjJqVGVRc1BrSlpodGp0dXdUVXJLMW81YVZFc3ZnT2dHOHBvbnRzaFRzZkEyNENuU2dYMWdiMkpSakovQUpaUmM1N3ZKSHg4Tm1FMmdpRkYzdlh3ZTlab2lyVm5OTVUyZENibGlUcXVhaHd1RWlWanEzRTZNTHZDUWpONlBQTjJXRG5jYTR4MGZOZVMxZm1rMHUzSTdwYk5EOXNoQVVSbE9RY0JROHp3dkhQVVBhL0kxVGkxNm5oZyIsImlhdCI6MTY1NTQ0NTg0NCwiZXhwIjoxNjU2NjU1NDQ0fQ.-UUM37mFP6D-H0virg6vlCCKCHP6oPA87Z5cJvVuT8o',
    'v': '1655481326',
    '_mlocation': '621540',
    '_mlocation_mode': 'default',
    'f': '5.c9152a8b62d51ee0af89b906f9d80c7916d443061c57ac4216d443061c57ac4216d443061c57ac4216d443061c57ac42cec4d980e289734fcec4d980e289734fcec4d980e289734f96a296658223dafb96a296658223dafb381ebd593ffbb4c30df103df0c26013a8b1472fe2f9ba6b90df103df0c26013a0df103df0c26013adc5322845a0cba1a4e312a1f8bb9ba1fbcc8809df8ce07f640e3fb81381f359178ba5f931b08c66a59b49948619279110df103df0c26013a2ebf3cb6fd35a0ac91e52da22a560f550df103df0c26013a7b0d53c7afc06d0bba0ac8037e2b74f92da10fb74cac1eab71e7cb57bbcb8e0f71e7cb57bbcb8e0f71e7cb57bbcb8e0f0df103df0c26013a03c77801b122405c868aff1d7654931c9d8e6ff57b051a581077304c7b13ca5d9538c5b98199aa03021dce8db01be7bf6c57406dd1bfe71ea4069f93e025cdf8aff5a88f928bb65f67a1b7ffdb90340fc215c537d24a43c80df103df0c26013a0df103df0c26013aafbc9dcfc006bed9fc1167f57e463df60d0b6fcb80ec00983de19da9ed218fe23de19da9ed218fe2d6fdecb021a45a31b3d22f8710f7c4ed78a492ecab7d2b7f',
    'ft': '"JWQx6KoerMjsM14m7Vcb+dep6hj9eEb7ENdYesqNZx4meTTpCO0K5L02Pq9kNeF6KB+Jtji01JljhyLpzNNPj6a1bmKph8PX6pimGRvyncgGFkJHJr4ytA9yl9EGnJDlTBuvmrtaQYLedd7jL9Km2Pn1Zm8/VrXWLraSHx/LSsHZnR9VHG5Av6vLZGsaWbh5"',
    'tmr_detect': '0%7C1655482837650',
    'luri': 'moskva',
    'sx': 'H4sIAAAAAAACA53SS3LjMAwE0LtonQVIgiTg2%2FAnWaYVyqHGlJzy3UeaqqSS5fgCrxrd%2BOyEFcpQxB4ZFVgD1nnsg%2BNgjbbM3emzu3enzli6XK5KLQN%2FfMQ0Rl1n5x8AXKJ9X7u3LnUnYbTWisni861DNE5rZwG9SKR6GxIHqVD0REkG%2BpIZ7SjGWNLNX%2FO9LSZmUXyMaPO2gvsls9W7rFmIpFJgksSJTXTe%2BT765I20MoUv2cbwuC%2Fz1PK8DGimG8y38%2BzOaprBrO2HLDWzOuS7FSuvl8efEKgC4jCUXEur%2F08qqf6RpM%2FSTkxN1ow5QCWE1lotL6Q0QhzNshdC9C5Yr%2FnIji4ACNjLAUVgvpvFyTSNt5l8fD9%2FWB6HzbtrlpNepn3onzIKJQ%2B5uIfEsKRbzVRLza0OuYXyHdZsXEPbbncRoGQKx0WtAAIB1eF3WGN4J921KJdDD1TaXmTAAXOFNsALKTXxQYZtnB9pxm1FJMyENIQhQ35hJCZNu1j0aoyGftSN8pBLLuF4gPbK7ALl8%2FkXjAHftFkDAAA%3D',
    'cto_bundle': '96etsF81ZnlMNFBLT1ZwTmNRemRVVnZtWkY4WXhlOFclMkJyTzI5RnBaQnNzT3owd081cWpMbUtpJTJGR3ZWb3FHamlkMVZyVFdjajcyUWhLZ2RlQ3NDNmt4a2Y0S0hHZXlvTXZ1VHhEd0ttOEc2OEhZcExjYVdWM0tPekt1RTMwM3NiRjE1V3hUQnd6azJja2tXcnRndGxKMXVqR2RRJTNEJTNE',
    '_ga': 'GA1.2.934049770.1655027495',
    '_ga_9E363E7BES': 'GS1.1.1655482818.16.1.1655486265.60',
    'tmr_reqNum': '271',
    }

headers = {
    'authority': 'm.avito.ru',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json;charset=utf-8',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'u=2tciqu1q.qe5y8h.fwquxt59heg0; _ym_d=1655027494; _ym_uid=165502749412228827; _gcl_au=1.1.366694497.1655027494; tmr_lvidTS=1655027494729; tmr_lvid=602d1e9fe65a87c9f458933b1e1f76d0; adrcid=AdVZ9AZcyhSLX0PRJo_fDag; uxs_uid=04d9a9f0-ea36-11ec-82d1-a96559ad0bb1; buyer_laas_location=637640; abp=0; buyer_location_id=637640; _gid=GA1.2.1527182154.1655369357; _ym_isad=2; isCriteoSetNew=true; st=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoidko0TkJ5SlU2TElJTGRDY3VNTkdBZm5PRWwySzdtS01KZXBFMDh1VUFISmJCTzdXeTdabjByWm5uVERhZHl5YVdUU0JDNkhibUszazZ5VnEyYWlnbTQralBzZFNrcGYrWFFYZmxPZ1doMXFzM1BQc0dOWUZQUllUeUFheCtJbktHdWhqQk0vbklVdlFyUllDdnZnaU5FdzlVbXVQRkxSV0ZoUTVvL0Q2ZkdRS2RyMzV2V04yUnY2SWFiU3U0L3VNT3RHbklXWnFsZkh4SDFYVWpmSUN2ZElFeEdySDJRM2VCY1BxellmNTBZRWU2ZWVzc2RjY0ppNm1aaUFKQjVJcE9hOEFSNFVPZHlrTThuajhGRHJUd2xzZ3pDRkNxUm9OYzFKVmRXOFVnYnJhOUNxOEZrUkhjWkpNYWtLcmUwMVhIc05YZENoN2ZxSDl3Rk9MZkxoT0RDbk1OL20yUzhYamppR0s2QmlHaUdQUFlwUStOT0RTWjg2c1V1NjhxcUhnZktrY3VaSkI3dHMzcWdrTXlxVDJoVFMwdlBwbWEwczhlSHBpcUVIaU1jL0U2bVVWQWhXQjkzNkFzTGhPSzNtRWMrdmx2OFRLMkVYYUJOU084djFESm1OcFpBbGFpbXRrOEs2UUo0QnRCMGpCK1lIN1ZzaENzUlhHMk1IZGk0RXBpblNma21iT1Jvb2FOazhBK1NRRUV6YjVTMG1QeGZNeGZ0cFlteFFjbFdVcWhXQmN3RkVWbk5hZEIvc1M0TWk0L0pzZ0lnSlBXaElnNWdOSVUvS3lnVzRueTlWcE95cXNuSmxUSitPTks2eVQwejFGMnVBSmt2cm5XREhvZ2RhZ2RpRHBwVUwzaDNyOU9uL0E3VldYeXFLeHc4bGxBRlp1cWFuSkE0d1A5bGxWSHUxUGptai9JTWZFcDc5dzhQTGVEQ2F6VGp0M3VCVlZDd2E5d2syM3VlRFJHdVJTOXUxTHY5TXhzc01CMnVHYVVHeHNaRHJwNDJrdkN2WndMTWM2L21RaVpKeDRVdlpicXoxaVh2NTlCM3pDN0RYZ2luOCtyWXl1a0liNlljMTdhcGZkTFpjc2UxUGo5T3FnQnVFeng2Rlo0QTF6ckt0VjZqZEcyaHdpcWdqQ1NQN3JsK1p3Y0tBelVvc2hhTElZYnVwWFROc2NlemNpL011T1UydnpiSWZNeTcyS1ZZY29IZHYvT1VlM3J4TVBIZURPNDQ5cldVVnhHVi9GcUlXVmE5c3JjV01ibVZVVGRIbVpBQnBrZlorR3g5dTdjK3l4bFpBRklSMXA0d3c0Zy9RL2hvZlFYR2FmMGJIZGhoMFJLV1lMbzlMNk5KVFRtY0JJMm1jbExOV01keUNyUjJqVGVRc1BrSlpodGp0dXdUVXJLMW81YVZFc3ZnT2dHOHBvbnRzaFRzZkEyNENuU2dYMWdiMkpSakovQUpaUmM1N3ZKSHg4Tm1FMmdpRkYzdlh3ZTlab2lyVm5OTVUyZENibGlUcXVhaHd1RWlWanEzRTZNTHZDUWpONlBQTjJXRG5jYTR4MGZOZVMxZm1rMHUzSTdwYk5EOXNoQVVSbE9RY0JROHp3dkhQVVBhL0kxVGkxNm5oZyIsImlhdCI6MTY1NTQ0NTg0NCwiZXhwIjoxNjU2NjU1NDQ0fQ.-UUM37mFP6D-H0virg6vlCCKCHP6oPA87Z5cJvVuT8o; v=1655481326; _mlocation=621540; _mlocation_mode=default; f=5.c9152a8b62d51ee0af89b906f9d80c7916d443061c57ac4216d443061c57ac4216d443061c57ac4216d443061c57ac42cec4d980e289734fcec4d980e289734fcec4d980e289734f96a296658223dafb96a296658223dafb381ebd593ffbb4c30df103df0c26013a8b1472fe2f9ba6b90df103df0c26013a0df103df0c26013adc5322845a0cba1a4e312a1f8bb9ba1fbcc8809df8ce07f640e3fb81381f359178ba5f931b08c66a59b49948619279110df103df0c26013a2ebf3cb6fd35a0ac91e52da22a560f550df103df0c26013a7b0d53c7afc06d0bba0ac8037e2b74f92da10fb74cac1eab71e7cb57bbcb8e0f71e7cb57bbcb8e0f71e7cb57bbcb8e0f0df103df0c26013a03c77801b122405c868aff1d7654931c9d8e6ff57b051a581077304c7b13ca5d9538c5b98199aa03021dce8db01be7bf6c57406dd1bfe71ea4069f93e025cdf8aff5a88f928bb65f67a1b7ffdb90340fc215c537d24a43c80df103df0c26013a0df103df0c26013aafbc9dcfc006bed9fc1167f57e463df60d0b6fcb80ec00983de19da9ed218fe23de19da9ed218fe2d6fdecb021a45a31b3d22f8710f7c4ed78a492ecab7d2b7f; ft="JWQx6KoerMjsM14m7Vcb+dep6hj9eEb7ENdYesqNZx4meTTpCO0K5L02Pq9kNeF6KB+Jtji01JljhyLpzNNPj6a1bmKph8PX6pimGRvyncgGFkJHJr4ytA9yl9EGnJDlTBuvmrtaQYLedd7jL9Km2Pn1Zm8/VrXWLraSHx/LSsHZnR9VHG5Av6vLZGsaWbh5"; tmr_detect=0%7C1655482837650; luri=moskva; sx=H4sIAAAAAAACA53SS3LjMAwE0LtonQVIgiTg2%2FAnWaYVyqHGlJzy3UeaqqSS5fgCrxrd%2BOyEFcpQxB4ZFVgD1nnsg%2BNgjbbM3emzu3enzli6XK5KLQN%2FfMQ0Rl1n5x8AXKJ9X7u3LnUnYbTWisni861DNE5rZwG9SKR6GxIHqVD0REkG%2BpIZ7SjGWNLNX%2FO9LSZmUXyMaPO2gvsls9W7rFmIpFJgksSJTXTe%2BT765I20MoUv2cbwuC%2Fz1PK8DGimG8y38%2BzOaprBrO2HLDWzOuS7FSuvl8efEKgC4jCUXEur%2F08qqf6RpM%2FSTkxN1ow5QCWE1lotL6Q0QhzNshdC9C5Yr%2FnIji4ACNjLAUVgvpvFyTSNt5l8fD9%2FWB6HzbtrlpNepn3onzIKJQ%2B5uIfEsKRbzVRLza0OuYXyHdZsXEPbbncRoGQKx0WtAAIB1eF3WGN4J921KJdDD1TaXmTAAXOFNsALKTXxQYZtnB9pxm1FJMyENIQhQ35hJCZNu1j0aoyGftSN8pBLLuF4gPbK7ALl8%2FkXjAHftFkDAAA%3D; cto_bundle=96etsF81ZnlMNFBLT1ZwTmNRemRVVnZtWkY4WXhlOFclMkJyTzI5RnBaQnNzT3owd081cWpMbUtpJTJGR3ZWb3FHamlkMVZyVFdjajcyUWhLZ2RlQ3NDNmt4a2Y0S0hHZXlvTXZ1VHhEd0ttOEc2OEhZcExjYVdWM0tPekt1RTMwM3NiRjE1V3hUQnd6azJja2tXcnRndGxKMXVqR2RRJTNEJTNE; _ga=GA1.2.934049770.1655027495; _ga_9E363E7BES=GS1.1.1655482818.16.1.1655486265.60; tmr_reqNum=271',
    'referer': 'https://m.avito.ru/items/search?categoryId=23&params[200]=1055&params[121019]=2849878&params[121020]=2849880&locationId=637640&localPriority=1&footWalkingMetro=0&params[596]=6203&priceMin=15000&priceMax=20000&params[510-from-int]=18&params[512]=5305&params[110497]=1&params[1458]=1&owner[]=private&sort=date&withImagesOnly=1&isGeoProps=true&presentationType=serp',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
    'x-laas-timezone': 'Europe/Moscow',
    }


# def get_dict_params(url_str):
#     row = url_str.split('key=')[1]
#     key = row.split('&')[0]
#     param_str = row.replace(key + '&', '')
#     param_list = param_str.replace('\\', '').split('&')
#     param_list = [i.split('=') for i in param_list]
#     param_dict = {i[0]: i[1] for i in param_list}
#     param_dict['key'] = key
#     return f'key = "{key}" \nparams = {param_dict}'
#
#
# print(get_dict_params(url_str))


'-------------------------------------------------------------------------------------'
"""get key, params from print(get_dict_params(url_str))"""

key = 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'

# params work without key in it:
params = {
    'categoryId': '23',
    'params[200]': '1055',
    'params[121019]': '2849878',
    'params[121020]': '2849880',
    'locationId': '637640',
    'localPriority': '1',
    'footWalkingMetro': '0',
    'params[596]': '6203',
    'priceMin': '15000',
    'priceMax': '20000',
    'params[510-from-int]': '18',
    'params[512]': '5305',
    'params[110497]': '1',
    'params[1458]': '1',
    'owner[]': 'private',
    'sort': 'date',
    'withImagesOnly': '1',
    'isGeoProps': 'true',
    'page': '1',
    'lastStamp': '1655482800',
    'display': 'list',
    'limit': '30',
    }
