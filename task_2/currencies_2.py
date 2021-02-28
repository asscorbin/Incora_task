# Домашнє 2:
# Напишіть клас з ім'ям Ccy.
# Він має мати декілька валют "EUR", "UAH" та "USD" (може мати більше).
# Також має мати суму у конкретній валюті. Внизу вказано приклад користуванням класом.
# Як видно нижче мають бути реалізовані оператори додавання, віднімання і т.п..
# Однак якщо добавити екземпляри класів з різними валютами, то має відбуватися конвертація
# і на виході видавати суму (чи іншу операцію) та валюту в якій видає результат
#
# from currencies import Ccy
# v1 = Ccy(23.43, "EUR")
# v2 = Ccy(19.97, "USD")
# print(v1 + v2)
#
# In [ ]: print(v2 + v1)
# In [ ]: print(v1 + 3) # an int or a float is considered to be a EUR value
# In [ ]: print(3 + v1)
import config


class Ccy:
    currency_market = {"UAH_EUR": 0.030,"UAH_USD": 0.036, "USD_EUR": 0.83}

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        pass

    @staticmethod
    def comparison(first, second):
        if first > second:
            return 1
        elif second > first:
            return 2
        elif first == second:
            return 0
        else:
            print(config.message_error)

    @staticmethod
    def compare_currency(first, second):
        comparison_result = Ccy.comparison(Ccy.exchange(first), Ccy.exchange(second))

        if comparison_result == 1:
            return first.currency
        elif comparison_result == 2:
            return second.currency
        elif comparison_result == 0:
            return Ccy.select_final_currency(first, second)
        else:
            print(config.message_error)

    @staticmethod
    def select_final_currency(first, second):
        return "UAH"

    @staticmethod
    def exchange(obj, expected_currency=config.currency_for_compare):
        if obj.currency == expected_currency:
            return obj.amount
        else:
            pass

    def __add__(self, other):
        type_other = type(other)

        if type_other == object:
            # перевірка чи одинакові валюти
            if self.currency == other.currency:
                return f"{self.currency},{self.amount + other.amount}"

            else:
                # перевірка якої валюти більше
                comparison_currency = self.compare_currency(self, other)

                # якщо першої то другу переводимо в першу
                if comparison_currency == self.currency:
                    amount = self.amount + Ccy.exchange(other, self.currency)
                    return f"{self.currency}, {amount}"

                elif comparison_currency == other.currency:
                    amount = Ccy.exchange(self.amount) + other.amount
                    return f"{other.currency}, {amount}"

                else:
                    print(config.message_error)

        elif type_other == int or type_other == float:
            return f"{self.currency},{self.amount + other}"
        else:
            print(config.message_error)
