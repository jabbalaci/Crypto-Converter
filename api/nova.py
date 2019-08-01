"""
Nova Exchange API

Examples:

https://novaexchange.com/remote/faq/
"""

import json

import requests

import utils

URL = "https://novaexchange.com/remote/v2/"


def api_query(method) -> dict:
    if method.split('/')[0][0:6] == 'market':
        r = requests.get(URL + method + '/', timeout=60)
    #
    return r.json()


def api_query_with_curl(method) -> dict:
    if method.split('/')[0][0:6] == 'market':
        url = f"{URL}{method}/"
        cmd = f'curl --silent -G {url}'
        try:
            # print('#', cmd)
            response = utils.get_simple_cmd_output(cmd)
            # print('#', response)
            return json.loads(response)    # type: ignore
        except Exception as e:
            print(e)
            return dict()    # empty dictionary
    # endif

    return dict()    # empty dictionary

############
## public ##
############

def get_last_price(market='BTC_QST') -> float:
    # d = api_query(f"market/info/{market}")
    d = api_query_with_curl(f"market/info/{market}")
    last_price = float(d['markets'][0]['last_price'])
    #
    return last_price
