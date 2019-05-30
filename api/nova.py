"""
Nova Exchange API

Examples:

https://novaexchange.com/remote/faq/
"""

import requests

URL = "https://novaexchange.com/remote/v2/"


def api_query(method) -> dict:
    if method.split('/')[0][0:6] == 'market':
        r = requests.get(URL + method + '/', timeout=60)
    #
    return r.json()

############
## public ##
############

def get_last_price(market='BTC_QST') -> float:
    d = api_query(f"market/info/{market}")
    last_price = float(d['markets'][0]['last_price'])
    #
    return last_price
