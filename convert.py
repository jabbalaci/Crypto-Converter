#!/usr/bin/env python3

"""
Jabba's Crypto Conversion Tool
------------------------------

A simple CLI application for converting currencies (crypto and fiat).

Author:

Laszlo Szathmary, alias Jabba Laci, 2019
jabba.laci@gmail.com
https://github.com/jabbalaci
"""

import os
try:
    import readline    # doesn't exist under Windows
except:
    pass
from pprint import pprint
from typing import Optional, Tuple, Union

import utils
from api import cmc, nova

default_currencies = ('BTC', 'USD', 'EUR', 'HUF')
accepted_fiat = ('USD', 'EUR', 'HUF')
crypto_currencies = ('BTC', 'QST')
accepted_currencies = tuple(default_currencies + crypto_currencies)
accepted_currencies_with_sat = accepted_currencies + ('sat',)    # satoshi included

platform = utils.get_platform()

VERSION = '0.2'
PROMPT = '▶' if platform == 'linux' else '>'
PYTHON = "python"    # command that you use to launch Python in the terminal

class NotImplementedException(Exception):
    pass


def formatter_fiat(amount: float) -> str:
    return f"{amount:.2f}"


def formatter_crypto(amount: float) -> str:
    return f"{amount:.8f}"


def money_formatter(amount: float, currency: str) -> str:
    if currency in accepted_fiat:
        return formatter_fiat(amount)
    if currency in crypto_currencies:
        return formatter_crypto(amount)
    # else:
    raise NotImplementedException


def sat_to_btc(amount_sat: float) -> float:
    """
    The value is given in satoshi.
    """
    smallest_sat = 1
    largest_sat = 99999999
    #
    if not (smallest_sat <= amount_sat <= largest_sat):
        raise ValueError
    # else
    btc = amount_sat * 1e-8
    return btc


def my_convert(amount: float, from_currency: str, to_currency: str) -> Optional[float]:
    if (from_currency == 'QST') or (to_currency == 'QST'):
        one_qst_in_btc: float = nova.get_last_price()    # 1 QST has this price in BTC
        if from_currency == 'QST':
            value_in_btc: float = amount * one_qst_in_btc
            if to_currency == 'BTC':
                return value_in_btc
            else:
                return my_convert(value_in_btc, 'BTC', to_currency)
        # endif
        if to_currency == 'QST':
            value_in_btc: float = my_convert(amount, from_currency, 'BTC')    # type: ignore
            return value_in_btc / one_qst_in_btc
        # endif

    # else, if QST is not present neither on the left side, nor on the right side

    d = cmc.convert(amount, from_currency, to_currency)
    if d:
        price: float = d['data']['quote'][to_currency]['price']
        return price
    # else:
    return None


def convert_to_default_currencies(amount_str: str, from_currency: str, to_currencies=default_currencies) -> None:
    try:
        amount = float(amount_str)
    except ValueError:
        print("Error: the first thing should be the amount")
        print()
        return
    #
    if from_currency not in accepted_currencies_with_sat:
        print("Error: accepted currencies at the moment: {0}. Pay attention to upper and lower cases too.".format(", ".join(accepted_currencies_with_sat)))
        print()
        return

    if from_currency == 'sat':
        try:
            # sat = amount
            amount = sat_to_btc(amount)
            from_currency = 'BTC'
            # print("{sat} sat = {amount} BTC".format(
                # sat=sat, amount=money_formatter(amount, 'BTC'))
            # )
        except ValueError:
            print("Error: invalid satoshi value")
            print()
            return

    for to in to_currencies:
        if to == from_currency:    # don't convert something to the same currency
            continue
        # else:
        if to not in accepted_currencies:
            print(f"Error: '{to}' is an unknown currency")
            continue
        #
        price = my_convert(amount, from_currency, to)
        if price:
            try:
                print("{amount} {from_currency} = {price} {to}".format(
                    amount=money_formatter(amount, from_currency), from_currency=from_currency,
                    price=money_formatter(price, to), to=to)
                )
            except NotImplementedException:
                print("Error: not implemented. Maybe you want to use an unsupported currency.")
        else:
            print(f"{amount} {from_currency} = ??? (error, try again)")
        # endif
    # endfor
    print()


def convert_to_given_currencies(amount: str, from_currency: str, to_str: str, to_currencies: str) -> None:
    if to_str not in ('to', '->'):
        print("Error: something is wrong")
        print()
        return
    # else:
    to_currs = tuple(to_currencies.split(','))
    convert_to_default_currencies(amount, from_currency, to_currs)


def human_readable(number: str) -> str:
    """
    convert a number to a human-readable format, e.g. 1500000 -> 1_500_000
    """
    if number.isdigit() and str(int(number)) == number:    # if number (as a string) contains an int
        return "{:_}".format(int(number))
    # else:
    return "{:_}".format(float(number))


def print_header() -> None:
    text = f"Jabba's Crypto Converter v{VERSION} (h - help; q - quit)"
    print(text)
    print("=" * len(text))


def print_help() -> None:
    text = """
Example                 Meaning
-------                 -------
2100 sat                How much is 2100 satoshi?
0.1 BTC                 How much is 0.1 bitcoin?
1_000 HUF               How much is one thousand Hungarian Forint?
25 EUR                  How much is 25 euro?
145 EUR to BTC          convert 145 euro to bitcoin
200 USD to HUF          convert 200 USD to Forint
200 USD to BTC          convert 200 USD to bitcoin
1000 USD to BTC,EUR     convert 1000 USD to bitcoin and euro (No space after comma!)

p                       launch a Python subshell (if you need a calculator)
hr 250000               print the number in human-readable format: 250_000
q                       quit
""".strip()
    print("Accepted currencies:", ", ".join(accepted_currencies_with_sat))
    print()
    print(text)
    print()


def main() -> None:
    print_header()

    while True:
        try:
            inp = input(f"{PROMPT} ").strip()
            if inp == "":
                continue
        except (KeyboardInterrupt, EOFError):
            print()
            print("bye")
            break

        if inp == 'q':
            print("bye")
            break
        elif inp == 'h':
            print_help()
            continue
        elif inp == 'p':
            os.system(PYTHON)
            continue

        parts = inp.split()

        if parts[0] == 'hr':
            try:
                assert len(parts) == 2
                num = float(parts[1])
                print(human_readable(parts[1]))
                print()
                continue
            except:
                print("Error: something is wrong")
                raise
                print()
                continue

        if len(parts) == 1:
            print("Error: something is missing")
            print()
            continue
        elif len(parts) == 2:
            convert_to_default_currencies(*parts)
        elif len(parts) == 4:
            convert_to_given_currencies(*parts)
        else:
            print("Error: something is wrong")
            print()
            continue
    # endwhile


def check_api_key():
    key = os.environ.get("COINMARKETCAP_API")
    if not key:
        print("Error: your CoinMarketCap API key is not found")
        print("Tip: put your API key in the environment variable called COINMARKETCAP_API")
        exit(1)

##############################################################################

if __name__ == "__main__":
    check_api_key()
    main()
