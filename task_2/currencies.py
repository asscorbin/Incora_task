import config


class Ccy:
    currency_market = {"UAH": {"USD": 0.036, "EUR": 0.030},
                       "USD": {"UAH": 27.95, "EUR": 0.83},
                       "EUR": {"UAH": 33.74, "USD": 1.21}}

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        pass

    def __int__(self):
        return self.amount

    @staticmethod
    def comparison(first, second):
        if first > second:
            return 1
        elif second > first:
            return 2
        elif first == second:
            return 0

    @staticmethod
    def compare_currency(first, second):
        comparison_result = Ccy.comparison(Ccy.exchange(first), Ccy.exchange(second))

        if comparison_result == 1:
            return first.currency
        elif comparison_result == 2:
            return second.currency
        elif comparison_result == 0:
            return Ccy.select_final_currency(first, second)

    @staticmethod
    def select_final_currency(first, second):
        if first.currency > second.currency:
            return first.currency
        elif second.currency > first.currency:
            return second.currency
        else:
            print("Одинакові значення та валюти")
            return first.currency

    @classmethod
    def exchange(cls, obj, expected_currency=config.currency_for_compare):
        if obj.currency == expected_currency:
            return obj.amount
        else:
            return obj.amount * cls.currency_market[obj.currency][expected_currency]

    def __add__(self, other):
        type_other = type(other)

        if type_other is type(self):
            if self.currency == other.currency:
                return f"{self.currency},{self.amount + other.amount}"
            else:
                comparison_currency = self.compare_currency(self, other)

                if comparison_currency == self.currency:
                    amount = self.amount + Ccy.exchange(other, self.currency)
                    return f"{self.currency}, {amount}"

                elif comparison_currency == other.currency:
                    amount = Ccy.exchange(self, other.currency) + other.amount
                    return f"{other.currency}, {amount}"

        elif type_other is int or type_other is float:
            return f"{self.currency}, {str(self.amount + other)}"

    def check_sub_available(self):
        pass

    def __sub__(self):
        pass

    def __mul__(self):
        pass

    def __truediv__(self):
        pass

    def __eq__(self, other):
        pass

    def __gt__(self, other):
        pass
