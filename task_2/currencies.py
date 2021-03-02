from task_2.data import *

general_currency = "UAH"


class Ccy:
    currency_market = Currency()

    _calc = {"+": lambda a, b: a + b,
             "-": lambda a, b: a - b}

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f"{self.currency} {self.amount}"

    @staticmethod
    def comparison(first, second):
        if first > second:
            return 1
        elif second > first:
            return 2
        elif first == second:
            return 0

    def compare_currency(self, other):
        comparison_result = Ccy.comparison(Ccy.exchange(self),
                                           Ccy.exchange(other))
        if comparison_result == 1:
            return self.currency
        elif comparison_result == 2:
            return other.currency
        elif comparison_result == 0:
            return self.select_final_currency(other)

    def select_final_currency(self, other):
        if self.currency > other.currency:
            return self.currency
        elif other.currency > self.currency:
            return other.currency
        else:
            return self.currency

    @classmethod
    def exchange(cls, obj, expected_currency=general_currency):
        if obj.currency == expected_currency:
            return obj.amount
        else:
            coefficient = cls.currency_market.get_currency_coefficient(
                obj.currency,
                expected_currency)
            return obj.amount * coefficient

    # def operations_with_object(self, other, sign):
    #     if self.currency == other.currency:
    #         return f"{self.currency},{self.amount + other.amount}"
    #
    #     else:
    #         comparison_currency = self.compare_currency(other)
    #
    #         if comparison_currency == self.currency:
    #             amount = self._calc[sign](self.amount,
    #                                       Ccy.exchange(other, self.currency))
    #             return f"{self.currency}, {amount}"
    #
    #         elif comparison_currency == other.currency:
    #             amount = self._calc[sign](Ccy.exchange(self, other.currency),
    #                                       other.amount)
    #             return f"{other.currency}, {amount}"

    def operations_with_object(self, other, sign):
        if self.currency == other.currency:
            return f"{self.currency},{self.amount + other.amount}"

        else:
            comparison_currency = self.compare_currency(other)

            if comparison_currency == self.currency:
                tuple_ = (self.amount, Ccy.exchange(other, self.currency),
                          self.currency)
            else:
                tuple_ = (Ccy.exchange(self, other.currency), other.amount,
                          other.currency)

            amount = self._calc[sign](tuple_[0], tuple_[1])
            return f"{tuple_[2]}, {amount}"

    def __add__(self, other):
        if type(self) == type(other):
            return self.operations_with_object(other, "+")
        else:
            return f"{self.currency}, {self.amount + other}"

    def __radd__(self, other):
        if type(self) == type(other):
            return self.operations_with_object(other, "+")
        else:
            return f"{self.currency}, {self.amount + other}"

    def check_sub_available(self):
        pass

    def __sub__(self, other):
        if type(self) == type(other):
            return self.operations_with_object(other, "-")
        else:
            return f"{self.currency}, {self.amount - other}"

    def __rsub__(self, other):
        if type(self) == type(other):
            return self.operations_with_object(other, "-")
        else:
            return f"{self.currency}, {self.amount - other}"

    # def __mul__(self, other):
    #     if type(self) == type(other):
    #         return self.operations_with_object(other, "*")
    #     else:
    #         return f"{self.currency}, {self.amount * other}"
    #
    # def __rmul__(self, other):
    #     if type(self) == type(other):
    #         return self.operations_with_object(other, "*")
    #     else:
    #         return f"{self.currency}, {self.amount * other}"
    #
    # def __truediv__(self, other):
    #     if type(self) == type(other):
    #         return self.operations_with_object(other, "/")
    #     else:
    #         return f"{self.currency}, {self.amount / other}"
    #
    # def __rtruediv__(self, other):
    #     if type(self) == type(other):
    #         return self.operations_with_object(other, "/")
    #     else:
    #         return f"{self.currency}, {self.amount / other}"

    def __eq__(self, other):
        self.compare_currency(other)

    def __gt__(self, other):
        pass
