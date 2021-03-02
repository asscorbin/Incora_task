import requests
import json

EUR = 978
USD = 840
UAH = 980
round_coefficient = 3
data_json = "data.json"

data = {"UAH": {"USD": 0, "EUR": 0},
        "USD": {"UAH": 0, "EUR": 0},
        "EUR": {"UAH": 0, "USD": 0}}


def get_currency_market_data():
    response = requests.get("https://api.monobank.ua/bank/currency").json()

    if response is list:
        with open(data_json, "w") as outfile:
            json.dump(response, outfile)
    else:
        with open(data_json, "r") as json_file:
            response = json.load(json_file)

    for index in response:
        if index["currencyCodeA"] == USD and index["currencyCodeB"] == UAH:
            data["USD"]["UAH"] = index["rateBuy"]
            data["UAH"]["USD"] = round(1 / index["rateSell"],
                                       round_coefficient)
        elif index["currencyCodeA"] == EUR and index["currencyCodeB"] == USD:
            data["EUR"]["USD"] = index["rateBuy"]
            data["USD"]["EUR"] = index["rateSell"]
        elif index["currencyCodeA"] == EUR and index["currencyCodeB"] == UAH:
            data["EUR"]["UAH"] = index["rateBuy"]
            data["UAH"]["EUR"] = round(1 / index["rateSell"],
                                       round_coefficient)

    return data


def get_currency_coefficient(from_, in_):
    data = get_currency_market_data()
    return data[from_][in_]
