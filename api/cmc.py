#!/usr/bin/env python3

"""
CoinMarketCap API
"""

import os
from typing import List, Union

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects


API_KEY = os.environ.get("COINMARKETCAP_API")

headers = {
    'Accepts': 'application/json',
    'Accept-Encoding': 'deflate, gzip',
    'X-CMC_PRO_API_KEY': API_KEY,
}

session = Session()
session.headers.update(headers)    # type: ignore


def api_call(url: str, parameters: dict) -> dict:
    try:
        response = session.get(url, params=parameters)
        return response.json()        # type: ignore
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        return dict()    # empty dictionary


def convert(amount: Union[int, float], from_currency: str, to_currency: str) -> Union[dict, List[dict]]:
    """
    Example:

    amount = 0.03
    from_currency = 'BTC'
    to_currency = 'USD,EUR,HUF'
    """
    url = 'https://pro-api.coinmarketcap.com/v1/tools/price-conversion'
    to_lst = to_currency.split(',')
    parameters = {
        'amount': amount,
        'symbol': from_currency,
    }
    result = []
    for to in to_lst:
        parameters['convert'] = to
        d = api_call(url, parameters)
        result.append(d)
    #
    if len(result) == 1:
        return result[0]
    else:
        return result
