from task_2.data import *
from functools import total_ordering


@total_ordering
class Ccy:
    currency_market = Currency()

    _calc = {"+": lambda a, b: a + b,
             "-": lambda a, b: a - b,
             "*": lambda a, b: a * b,
             "/": lambda a, b: a / b}

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
    def exchange(cls, obj, expected_currency=config.currency_for_compare):
        if obj.currency == expected_currency:
            return obj.amount
        else:
            coefficient = cls.currency_market.get_currency_coefficient(
                obj.currency,
                expected_currency)
            return obj.amount * coefficient

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

    @staticmethod
    def check_sub_object_available(decreasing, subtractor):
        comparison_result = Ccy.comparison(Ccy.exchange(decreasing),
                                           Ccy.exchange(subtractor))

        return_ = True if comparison_result == 0 or comparison_result == 1 \
            else False

        return return_

    @staticmethod
    def check_sub_number_available(decreasing, subtractor):
        return 0 <= (decreasing - subtractor)

    def __sub__(self, other):
        if type(self) == type(other):
            if Ccy.check_sub_object_available(self, other):
                return self.operations_with_object(other, "-")
        else:
            if Ccy.check_sub_number_available(self.amount, other):
                return f"{self.currency}, {self.amount - other}"

        return config.subtraction_error

    def __rsub__(self, other):
        if type(self) == type(other):
            if Ccy.check_sub_object_available(other, self):
                return self.operations_with_object(other, "-")
        else:
            if Ccy.check_sub_number_available(other, self.amount):
                return f"{self.currency}, {self.amount - other}"

        print(config.subtraction_error)

    def __mul__(self, other):
        if type(self) == type(other):
            return self.operations_with_object(other, "*")
        else:
            return f"{self.currency}, {self.amount * other}"

    def __rmul__(self, other):
        if type(self) == type(other):
            return self.operations_with_object(other, "*")
        else:
            return f"{self.currency}, {self.amount * other}"

    @staticmethod
    def check_truediv_object_available(decreasing, subtractor):
        if subtractor == 0:
            return False
        comparison_result = Ccy.comparison(Ccy.exchange(decreasing),
                                           Ccy.exchange(subtractor))

        return_ = True if comparison_result == 0 or comparison_result == 1 \
            else False

        return return_

    @staticmethod
    def check_truediv_number_available(decreasing, subtractor):
        if subtractor == 0:
            return False
        return 0 <= (decreasing / subtractor)

    def __truediv__(self, other):
        if type(self) == type(other):
            return self.operations_with_object(other, "/")
        else:
            return f"{self.currency}, {self.amount / other}"

    def __rtruediv__(self, other):
        if type(self) == type(other):
            return self.operations_with_object(other, "/")
        else:
            return f"{self.currency}, {self.amount / other}"

    def __eq__(self, other):
        if other is type(self):
            return Ccy.exchange(self) == Ccy.exchange(other)
        else:
            return Ccy.exchange(self) == other

    def __gt__(self, other):
        if isinstance(other, type(self)):
            return Ccy.exchange(self) > Ccy.exchange(other)
        else:
            return Ccy.exchange(self) > other
