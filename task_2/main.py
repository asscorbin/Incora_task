from task_2.currencies import Ccy

uah = Ccy(100, "UAH")
usd = Ccy(100, "USD")

print(" *** + *** ")
print(uah + usd)
print(uah + 100)
print(100 + uah)
print(" *** - *** ")
print(uah - usd)
print(uah - 100)
print(100 - uah)
