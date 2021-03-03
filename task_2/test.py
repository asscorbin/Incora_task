from task_2.currencies import Ccy


def check_sub_object_available(decreasing, subtractor):
    comparison_result = Ccy.comparison(Ccy.exchange(decreasing),
                                       Ccy.exchange(subtractor))

    return_ = True if comparison_result == 0 or comparison_result == 1 \
        else False

    return return_

c = Ccy(100,"UAH")
b = Ccy(200, "UAH")

print(check_sub_object_available(c,b))
print(check_sub_object_available(b,c))
print(check_sub_object_available(c,c))


