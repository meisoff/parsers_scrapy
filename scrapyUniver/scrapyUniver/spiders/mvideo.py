import scrapy
from urllib.parse import urlencode
import requests

class MvideoSpider(scrapy.Spider):
    name = 'mvideo'
    allowed_domains = ['www.mvideo.ru']
    start_urls = ['https://www.mvideo.ru/']
    cookies = {
        '_ym_uid': '1653128843717093396',
        '_ym_d': '1653128843',
        'COMPARISON_INDICATOR': 'false',
        'HINTS_FIO_COOKIE_NAME': '1',
        'MVID_AB_SERVICES_DESCRIPTION': 'var2',
        'MVID_ADDRESS_COMMENT_AB_TEST': '2',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
        'MVID_CART_MULTI_DELETE': 'true',
        'MVID_CATALOG_STATE': '1',
        'MVID_CHECKOUT_REGISTRATION_AB_TEST': '2',
        'MVID_CITY_ID': 'CityCZ_2030',
        'MVID_EXP_NEW_RANKING': '1',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_GUEST_ID': '21364059218',
        'MVID_HANDOVER_SUMMARY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '6600000100000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_MCLICK': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_MOBILE_FILTERS': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_REGION_ID': '5',
        'MVID_REGION_SHOP': 'S953',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'new',
        'MVID_TIMEZONE_OFFSET': '5',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'searchType2': '3',
        '__SourceTracker': 'google__organic',
        'admitad_deduplication_cookie': 'google__organic',
        'tmr_lvid': '0aa2ceaa73b899ea9534bdca77cc0e0e',
        'tmr_lvidTS': '1662048378701',
        'flocktory-uuid': '407c0385-eb3c-4e60-b844-35a4ef36ee25-7',
        'afUserId': 'e26fe183-44a1-41c4-92dd-55c173d9b1ab-p',
        'uxs_uid': '06b98be0-2a10-11ed-8b60-6d0227f353ac',
        'wurfl_device_id': 'generic_web_browser',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        'MVID_CART_AVAILABILITY': 'true',
        'MVID_CREDIT_AVAILABILITY': 'true',
        'mindboxDeviceUUID': '1e88393a-eeaa-4b0d-8667-60d70563d29c',
        'directCrm-session': '%7B%22deviceGuid%22%3A%221e88393a-eeaa-4b0d-8667-60d70563d29c%22%7D',
        '__lhash_': '5f0c32b5c3610d1ee0da53b5b0884585',
        'MVID_AB_PDP_CHAR': '1',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_GLP': 'true',
        'MVID_LP_HANDOVER': '1',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'flacktory': 'no',
        '_gid': 'GA1.2.777866407.1663604223',
        '_ym_isad': '1',
        'advcake_track_id': '2a520ef7-75c7-703f-e28e-79417bbd1b7d',
        'advcake_session_id': 'ff985cdd-090e-e2b8-00e7-b931136a6b15',
        'AF_SYNC': '1663604228454',
        '__ttl__widget__ui': '1663606731917-61fba086ee48',
        'cookie_ip_add': '92.248.185.240',
        'MVID_GEOLOCATION_NEEDED': 'false',
        'BIGipServeratg-ps-prod_tcp80': '1157946378.20480.0000',
        'bIPs': '-1178626581',
        'MVID_GTM_BROWSER_THEME': '1',
        'deviceType': 'tablet',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VpCyFXIQ9gRkVzTRg/OlEjLjoLHzIfWREXHmxiFj4tXR5beXdtS2U3VzwQaiApEilPdxsxGjhmI2JJXSdKWE8KFhoXfW4pUw0QYD1JcnsbN1ddHBEkWA4hPwtpW1Y0ZxUbQEgYL0tueS8+ayFlTF4kR1VVdRdgSkMrNhZGRhxyM3c/awgiGVETKl94R1drZVVCODFnDE9PTRIW2FG50A==',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VpCyFXIQ9gRkVzTRg/OlEjLjoLHzIfWREXHmxiFj4tXR5beXdtS2U3VzwQaiApEilPdxsxGjhmI2JJXSdKWE8KFhoXfW4pUw0QYD1JcnsbN1ddHBEkWA4hPwtpW1Y0ZxUbQEgYL0tueS8+ayFlTF4kR1VVdRdgSkMrNhZGRhxyM3c/awgiGVETKl94R1drZVVCODFnDE9PTRIW2FG50A==',
        'SMSError': '',
        'authError': '',
        'cfidsgib-w-mvideo': 'QP5EcyATqlhCiUdlpolsJVz3WGyTkUzt3w2pOcStXHgxFKb8xYOpamOJPdYqYrh8BBIFVFZVJkAzgFydNHnQh0xmkuMAuYatmUlSPOMOvDnFdMFthjf6LXvB4bbJaNjiPeAUGw2CSHlBc9GkuXSEjVInOmph6sVXMpB6mA==',
        'cfidsgib-w-mvideo': 'QP5EcyATqlhCiUdlpolsJVz3WGyTkUzt3w2pOcStXHgxFKb8xYOpamOJPdYqYrh8BBIFVFZVJkAzgFydNHnQh0xmkuMAuYatmUlSPOMOvDnFdMFthjf6LXvB4bbJaNjiPeAUGw2CSHlBc9GkuXSEjVInOmph6sVXMpB6mA==',
        'gsscgib-w-mvideo': 'My0GRZgyoNOobG695ZTELZdieRxpJYh1nnIvcJg3gfqCz8tvHWD4FBRRRQntFm5itaQlw+OGnkyzmfr74pPlrBUO8EJ55VehdpU3n/USKAL4BfhIWoFkR9URRys4fOzCkWejz3W6v0U5i/NkX08JT0AaRbzpd6UDZQYL6n8z02TKeWJanFyPwardsEAAUWyzNZ2l53we6NG7Td5A1XCDPZhzAJAFRVPB4W52Pc4NTV4WGM751kz185U31xcB2miFmw==',
        'gsscgib-w-mvideo': 'My0GRZgyoNOobG695ZTELZdieRxpJYh1nnIvcJg3gfqCz8tvHWD4FBRRRQntFm5itaQlw+OGnkyzmfr74pPlrBUO8EJ55VehdpU3n/USKAL4BfhIWoFkR9URRys4fOzCkWejz3W6v0U5i/NkX08JT0AaRbzpd6UDZQYL6n8z02TKeWJanFyPwardsEAAUWyzNZ2l53we6NG7Td5A1XCDPZhzAJAFRVPB4W52Pc4NTV4WGM751kz185U31xcB2miFmw==',
        'fgsscgib-w-mvideo': 'z6ho3f138f2ba81058d6e8f744ec447e6741c9f3',
        'fgsscgib-w-mvideo': 'z6ho3f138f2ba81058d6e8f744ec447e6741c9f3',
        'cfidsgib-w-mvideo': 'O/ME5doC10ahMwKcJ3dPW9aAJaMu4B+rQdoVhekXmGVxL9xSORSVBc/N+me8Ga623BOQ70vaaJzKiJCvpIXpv1JBBOpbwuJDmfrRbzIKnYqr8sLoT2RMk5m5uFCbpwp9tng5aPNWjrBhfp1uVxVqjf4pbeu6wmTERgq4YA==',
        'CACHE_INDICATOR': 'false',
        '_sp_id.d61c': '7a5b7a50-2ca2-4f87-92b2-50576edcf712.1662048376.8.1663646584.1663615213.18dbe9c0-9fea-4552-8568-2d71a1315487.a76580a7-3dc9-4f78-bc11-f6a58cbe4cbc.f8940e4a-030f-4d43-80e7-281175598afc.1663646292547.4',
        '_ga': 'GA1.2.503802561.1662048376',
        'tmr_detect': '1%7C1663646587546',
        'tmr_reqNum': '177',
        '__hash_': '7745c54132d5e2f2196f0d195fb70bf6',
        'JSESSIONID': 'h23MjphXrHvkpwp1DWMl3WQsvV6Qh1nZByfqHmQkqvnLgPc11RfJ!-3914716',
        '_ga_CFMZTSS5FM': 'GS1.1.1663656248.10.0.1663656248.0.0.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1663656248.10.0.1663656248.60.0.0',
        'MVID_ENVCLOUD': 'prod2',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'baggage': 'sentry-transaction=%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=6fd87fed9c4543d9b0fff984a3857fbe,sentry-sample_rate=0%2C5',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ym_uid=1653128843717093396; _ym_d=1653128843; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=1; MVID_AB_SERVICES_DESCRIPTION=var2; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=true; MVID_CART_MULTI_DELETE=true; MVID_CATALOG_STATE=1; MVID_CHECKOUT_REGISTRATION_AB_TEST=2; MVID_CITY_ID=CityCZ_2030; MVID_EXP_NEW_RANKING=1; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GUEST_ID=21364059218; MVID_HANDOVER_SUMMARY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=6600000100000; MVID_LAYOUT_TYPE=1; MVID_MCLICK=true; MVID_MINI_PDP=true; MVID_MOBILE_FILTERS=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_REGION_ID=5; MVID_REGION_SHOP=S953; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; MVID_TIMEZONE_OFFSET=5; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; searchType2=3; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; tmr_lvid=0aa2ceaa73b899ea9534bdca77cc0e0e; tmr_lvidTS=1662048378701; flocktory-uuid=407c0385-eb3c-4e60-b844-35a4ef36ee25-7; afUserId=e26fe183-44a1-41c4-92dd-55c173d9b1ab-p; uxs_uid=06b98be0-2a10-11ed-8b60-6d0227f353ac; wurfl_device_id=generic_web_browser; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; MVID_CART_AVAILABILITY=true; MVID_CREDIT_AVAILABILITY=true; mindboxDeviceUUID=1e88393a-eeaa-4b0d-8667-60d70563d29c; directCrm-session=%7B%22deviceGuid%22%3A%221e88393a-eeaa-4b0d-8667-60d70563d29c%22%7D; __lhash_=5f0c32b5c3610d1ee0da53b5b0884585; MVID_AB_PDP_CHAR=1; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_GLP=true; MVID_LP_HANDOVER=1; MVID_LP_SOLD_VARIANTS=3; MVID_MINDBOX_DYNAMICALLY=true; MVID_PROMO_CATALOG_ON=true; flacktory=no; _gid=GA1.2.777866407.1663604223; _ym_isad=1; advcake_track_id=2a520ef7-75c7-703f-e28e-79417bbd1b7d; advcake_session_id=ff985cdd-090e-e2b8-00e7-b931136a6b15; AF_SYNC=1663604228454; __ttl__widget__ui=1663606731917-61fba086ee48; cookie_ip_add=92.248.185.240; MVID_GEOLOCATION_NEEDED=false; __hash_=7745c54132d5e2f2196f0d195fb70bf6; _sp_ses.d61c=*; JSESSIONID=pxdjjp7W2N0GJQpTkGdHWlLxRSsWYQvFmlfRPzpNvmMwyR7vBfVf!-1632487329; BIGipServeratg-ps-prod_tcp80=1157946378.20480.0000; bIPs=-1178626581; MVID_GTM_BROWSER_THEME=1; deviceType=tablet; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VpCyFXIQ9gRkVzTRg/OlEjLjoLHzIfWREXHmxiFj4tXR5beXdtS2U3VzwQaiApEilPdxsxGjhmI2JJXSdKWE8KFhoXfW4pUw0QYD1JcnsbN1ddHBEkWA4hPwtpW1Y0ZxUbQEgYL0tueS8+ayFlTF4kR1VVdRdgSkMrNhZGRhxyM3c/awgiGVETKl94R1drZVVCODFnDE9PTRIW2FG50A==; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VpCyFXIQ9gRkVzTRg/OlEjLjoLHzIfWREXHmxiFj4tXR5beXdtS2U3VzwQaiApEilPdxsxGjhmI2JJXSdKWE8KFhoXfW4pUw0QYD1JcnsbN1ddHBEkWA4hPwtpW1Y0ZxUbQEgYL0tueS8+ayFlTF4kR1VVdRdgSkMrNhZGRhxyM3c/awgiGVETKl94R1drZVVCODFnDE9PTRIW2FG50A==; SMSError=; authError=; cfidsgib-w-mvideo=QP5EcyATqlhCiUdlpolsJVz3WGyTkUzt3w2pOcStXHgxFKb8xYOpamOJPdYqYrh8BBIFVFZVJkAzgFydNHnQh0xmkuMAuYatmUlSPOMOvDnFdMFthjf6LXvB4bbJaNjiPeAUGw2CSHlBc9GkuXSEjVInOmph6sVXMpB6mA==; cfidsgib-w-mvideo=QP5EcyATqlhCiUdlpolsJVz3WGyTkUzt3w2pOcStXHgxFKb8xYOpamOJPdYqYrh8BBIFVFZVJkAzgFydNHnQh0xmkuMAuYatmUlSPOMOvDnFdMFthjf6LXvB4bbJaNjiPeAUGw2CSHlBc9GkuXSEjVInOmph6sVXMpB6mA==; gsscgib-w-mvideo=My0GRZgyoNOobG695ZTELZdieRxpJYh1nnIvcJg3gfqCz8tvHWD4FBRRRQntFm5itaQlw+OGnkyzmfr74pPlrBUO8EJ55VehdpU3n/USKAL4BfhIWoFkR9URRys4fOzCkWejz3W6v0U5i/NkX08JT0AaRbzpd6UDZQYL6n8z02TKeWJanFyPwardsEAAUWyzNZ2l53we6NG7Td5A1XCDPZhzAJAFRVPB4W52Pc4NTV4WGM751kz185U31xcB2miFmw==; gsscgib-w-mvideo=My0GRZgyoNOobG695ZTELZdieRxpJYh1nnIvcJg3gfqCz8tvHWD4FBRRRQntFm5itaQlw+OGnkyzmfr74pPlrBUO8EJ55VehdpU3n/USKAL4BfhIWoFkR9URRys4fOzCkWejz3W6v0U5i/NkX08JT0AaRbzpd6UDZQYL6n8z02TKeWJanFyPwardsEAAUWyzNZ2l53we6NG7Td5A1XCDPZhzAJAFRVPB4W52Pc4NTV4WGM751kz185U31xcB2miFmw==; _dc_gtm_UA-1873769-1=1; _dc_gtm_UA-1873769-37=1; fgsscgib-w-mvideo=z6ho3f138f2ba81058d6e8f744ec447e6741c9f3; fgsscgib-w-mvideo=z6ho3f138f2ba81058d6e8f744ec447e6741c9f3; cfidsgib-w-mvideo=O/ME5doC10ahMwKcJ3dPW9aAJaMu4B+rQdoVhekXmGVxL9xSORSVBc/N+me8Ga623BOQ70vaaJzKiJCvpIXpv1JBBOpbwuJDmfrRbzIKnYqr8sLoT2RMk5m5uFCbpwp9tng5aPNWjrBhfp1uVxVqjf4pbeu6wmTERgq4YA==; CACHE_INDICATOR=false; _sp_id.d61c=7a5b7a50-2ca2-4f87-92b2-50576edcf712.1662048376.8.1663646570.1663615213.18dbe9c0-9fea-4552-8568-2d71a1315487.a76580a7-3dc9-4f78-bc11-f6a58cbe4cbc.f8940e4a-030f-4d43-80e7-281175598afc.1663646292547.3; _ga=GA1.2.503802561.1662048376; tmr_detect=1%7C1663646574204; tmr_reqNum=166; _ga_CFMZTSS5FM=GS1.1.1663646286.9.1.1663646578.0.0.0; _ga_BNX5WPP3YK=GS1.1.1663646286.9.1.1663646579.33.0.0; MVID_ENVCLOUD=prod2',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '6fd87fed9c4543d9b0fff984a3857fbe-ad626e21c8fe0a2f-1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'x-set-application-id': '4990a5c7-7e6b-4f39-850c-5ec378bae591',
    }

    params = {
        'categoryId': '118',
        'offset': '0',
        'limit': '24',
        'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==',
        'doTranslit': 'true',
    }

    url = 'https://www.mvideo.ru/bff/products/listing' + '?' + urlencode(params)

    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse, cookies=self.cookies,
                             headers=self.headers)

    def parse(self, response):
        products = response.json()
        products_ids = products.get('body').get('products')
        json_data = {
            'productIds': products_ids,
            'mediaTypes': [
                'images',
            ],
            'category': True,
            'status': True,
            'brand': True,
            'propertyTypes': [
                'KEY',
            ],
            'propertiesConfig': {
                'propertiesPortionSize': 5,
            },
            'multioffer': False,
        }

        params = {
            'productIds': ','.join(products_ids),
            'addBonusRubles': 'true',
            'isPromoApplied': 'true',
        }
        # url = ('https://www.mvideo.ru/bff/products/prices' + '?' + urlencode(params, safe='%2C')).replace('%27', '').replace('+', '').replace('%5B', '').replace('%5D', '')

        # yield {
        #     'Information': scrapy.http.JsonRequest(url='https://www.mvideo.ru/bff/product-details/list',
        #                                           callback=self.parse_list,
        #                                           cookies=self.cookies, headers=self.headers, formdata=json_data),
        #     'Prices': scrapy.Request(url=url, callback=self.parse_price, cookies=self.cookies, headers=self.headers,
        #                            meta={'productsIds': products_ids}),
        # }
        yield self.parse_list(requests.post(url='https://www.mvideo.ru/bff/product-details/list',
                                                  cookies=self.cookies, headers=self.headers, json=json_data))

    def parse_list(self, response):
        items = response.json()
        for item in items.get('body').get('products'):
            product_id = item.get('productId')
            brand_name = item.get('brandName')
            category = item.get('category').get('name')
            model_name = item.get('modelName')
            name_translit = item.get('nameTranslit')
            properties_list = item.get('propertiesPortion')
            properties_portion = {
                f'{properties_list[0].name}': properties_list[0].value,
                f'{properties_list[1].name}': properties_list[1].value,
                f'{properties_list[2].name}': properties_list[2].value,
                f'{properties_list[3].name}': properties_list[3].value,
                f'{properties_list[4].name}': properties_list[4].value,
            }
            rating = round(item.rating.star, 2)

            yield {
                f'{product_id}': {
                    'brand_name': brand_name,
                    'category': category,
                    'model_name': model_name,
                    'name_translit': name_translit,
                    'properties_portion': properties_portion,
                    'rating': rating,
                }
            }

    def parse_price(self, response):
        products_ids = response.Request.meta('productsIds')
        prices = response.json()
        prices_obj = {}
        for product_id in products_ids:
            for price in prices.get('body').get('materialPrices'):
                if product_id == price.get('productId'):
                    price_list = {
                        'salePrice': price.get('price').get('salePrice'),
                        'basePrice': price.get('price').get('basePrice'),
                    }
                    prices_obj.update((product_id, price_list))
        return prices_obj
