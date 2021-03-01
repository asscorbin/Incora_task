from task_2.currencies import *

uah = Ccy(100, "UAH")
usd = Ccy(100, "USD")

print(uah + usd)
print(uah + 100)
print(100 + int(uah))
