# Домашка3:
# Треба реалізувати range через написання генератора
# з всім функціоналом range(start, stop, step).
# Тобто щоб можна було вводити:
# range(10)
# range(1, 10)
# range(1, 10, 2)
# і хто хоче складніший варіант:
# range(10, 1, -2)
import time


def time_check(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rest = func(*args, **kwargs)
        end = time.time()
        print('Час виконання'.format(end - start))
        return rest

    return wrapper


@time_check
def range_(start: int = 0, stop: int = 0, step: int = 1):
    if not all((isinstance(start, int), isinstance(stop, int),
                isinstance(step, int))):
        raise TypeError("object cannot be interpreted as an integer")
    while start < stop:
        if (start > stop and step > 0) or \
                (start < stop and step < 0):
            break
        yield start
        start += step
