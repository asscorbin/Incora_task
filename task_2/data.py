import datetime
import requests
import json

from task_2 import config


class Currency:
    data = {"UAH": {"USD": 0, "EUR": 0},
            "USD": {"UAH": 0, "EUR": 0},
            "EUR": {"UAH": 0, "USD": 0}}

    def __init__(self):
        self.last_data_update = datetime.datetime.now()
        self.get_currency_market_data()

    def get_currency_market_data(self):
        self.last_data_update = datetime.datetime.now()

        response = requests.get(config.API_address).json()

        if response is list:
            with open(config.data_json, "w") as outfile:
                json.dump(response, outfile)
        else:
            with open(config.data_json, "r") as json_file:
                response = json.load(json_file)

        for index in response:
            if index[config.CCA] == config.USD and \
                    index[config.CCB] == config.UAH:

                self.data["USD"]["UAH"] = index[config.rateBuy]
                self.data["UAH"]["USD"] = round(1 / index[config.rateSell],
                                                config.round_coefficient)
            elif index[config.CCA] == config.EUR and index[
                config.CCB] == config.USD:

                self.data["EUR"]["USD"] = index[config.rateBuy]
                self.data["USD"]["EUR"] = index[config.rateSell]
            elif index[config.CCA] == config.EUR and index[
                config.CCB] == config.UAH:

                self.data["EUR"]["UAH"] = index[config.rateBuy]
                self.data["UAH"]["EUR"] = round(1 / index[config.rateSell],
                                                config.round_coefficient)

        return self.data

    def check_necessity_data_updates(self):
        now = datetime.datetime.now()
        self.last_data_update += datetime.timedelta(hours=1)

        if now > self.last_data_update:
            self.get_currency_market_data()

    def get_currency_coefficient(self, from_, in_):
        self.check_necessity_data_updates()

        return self.data[from_][in_]
