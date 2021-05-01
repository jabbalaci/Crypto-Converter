Jabba's Crypto Converter
========================

A command-line application for converting currencies (crypto and fiat).

Examples
--------

```
$ ./convert.py
Jabba's Crypto Converter v0.2 (h - help; q - quit)
==================================================
▶ h
Accepted currencies: BTC, USD, EUR, HUF, BTC, QST, sat

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

▶ 2100 sat
0.00002100 BTC = 0.18 USD
0.00002100 BTC = 0.16 EUR
0.00002100 BTC = 52.66 HUF

▶ 0.1 BTC
0.10000000 BTC = 859.82 USD
0.10000000 BTC = 772.40 EUR
0.10000000 BTC = 250762.80 HUF

▶ 1_000 HUF
1000.00 HUF = 0.00039878 BTC
1000.00 HUF = 3.43 USD
1000.00 HUF = 3.08 EUR

▶ 25 EUR
25.00 EUR = 0.00323669 BTC
25.00 EUR = 27.83 USD
25.00 EUR = 8117.11 HUF

▶ 145 EUR to BTC
145.00 EUR = 0.01877281 BTC

▶ 200 USD to HUF
200.00 USD = 58334.00 HUF

▶ 200 USD to BTC
200.00 USD = 0.02326066 BTC

▶ 1000 USD to BTC,EUR
1000.00 USD = 0.11630328 BTC
1000.00 USD = 898.32 EUR

▶ p
Python 3.7.3 (default, Mar 26 2019, 21:43:19)
[GCC 8.2.1 20181127] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 898.32 * 1.15
1033.068
>>>
▶ 1033.068 EUR to USD
1033.07 EUR = 1149.99 USD

▶ 1 BTC to HUF
1.00000000 BTC = 2502407.48 HUF

▶ hr 2502407
2_502_407

▶ q
bye
```

Supported platforms
-------------------

The program was tested under Linux and Windows.

API key
-------

The application uses the API of [CoinMarketCap](https://coinmarketcap.com/). Register for free, visit [https://coinmarketcap.com/api](https://coinmarketcap.com/api), and then generate an API key for yourself. Then, add this key to an environment variable called ``COINMARKETCAP_API``.

Under Linux, for instance, add the following line to the end of your ``~/.bashrc`` file:

```
export COINMARKETCAP_API="<your_coinmarketcap_api_key_here>"
```

Creating the virtual environment
--------------------------------

I suggest using poetry.

Launching the application
-------------------------

Activate the virt. env. and then launch the program:

    $ poetry shell
    $ ./convert.py

Creating an executable
----------------------

    $ poetry shell
    $ make exe

The EXE will appear in the `dist/` folder. It will be a standalone exe that you can use anywhere (even on a machine that doesn't have Python at all), i.e. this exe is portable.

Use it at your own risk
-----------------------

Quote from the LICENSE file:

```
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
