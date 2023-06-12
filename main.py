import requests
from bs4 import BeautifulSoup


class CurrencyConverter:
    def __init__(self):
        self.url = 'https://bank.gov.ua/ua/markets/exchangerates'

    def get_exchange_rate(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')

        table = soup.find('table', class_='other-currency-table')

        usd_row = table.find('tr', attrs={'data-currency': 'USD'})

        rate = usd_row.find('td', class_='rate').text

        return float(rate)


converter = CurrencyConverter()
usd_rate = converter.get_exchange_rate()
print(f"Курс долара США: {usd_rate}")


class CurrencyConverter:
    def __init__(self, usd_rate):
        self.usd_rate = usd_rate

    def convert_to_usd(self, amount):
        return amount / self.usd_rate


converter = CurrencyConverter(usd_rate)
amount_in_local_currency = float(input("Введіть суму у вашій валюті: "))
amount_in_usd = converter.convert_to_usd(amount_in_local_currency)
print(f"Сума в доларах США: {amount_in_usd}")
''