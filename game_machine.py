import random


class GameMachine:

    # - Конструктор класу приймає один вхідний параметр: початкову суму грошей яка заноситься в автомат (number)
    def __init__(self, money):
        self.money = money

    # - геттер getMoney - отримати загальну суму грошей у GameMachine
    def get_money(self):
        # return self.money
        # Тут пхд має бути ітератор
        pass

    # - метод, щоб забрати з GameMachine гроші. Вхідний аргумент - сума (number)
    def take_money(self, money):
        self.money -= money
        return self.money

    # - Покласти гроші. Вхідний аргумент - сума (number)
    def put_money(self, money):
        self.money += money

    # - Зіграти. Вхідний аргумент - сума (number) грошей, яку гравець закидує в автомат.
    def spin(self, money):
        self.money += money

        # Генеруємо випадково 3-х значне число
        generated_number = str(random.randint(0, 999)).rjust(3, '0')
        print(generated_number)

        for i in generated_number:
            # Якщо у числі 2 цифри однакові, повертається сума у 2 рази більша ніж прийшла в аргументі (і віднімається
            # від суми грошей в автоматі)
            if generated_number.count(i) == 2:
                print("\t\tВи подвоїли свої кошти \n\t\t\t", generated_number)
                return money * 2

            # Якщо 3 цифри однакові - повертається 3-кратна сума
            elif generated_number.count(i) == 3:
                print("\t\tВи потроїли свої кошти \n\t\t\t", generated_number)
                return money * 3

        print("\t\tВи програли \n\t\t\t", generated_number)
        return 0

    def check_enough_money(self, money):
        if self.money >= int(money) * 3:
            return True
        else:
            return False


def print_all_available_game_mashine(all_casino):
    print("**** Виведення усіх ігрових автоматів ****"
          "\tНомер   -----   коштів")
    counter = 0
    for casino in all_casino:
        for game_machine in casino.game_machines:
            counter += 1
            print(f"\t  {counter}\t\t{game_machine.money}")


def delete_game_machine(all_casino, num_game_machine):
    counter = 0
    for casino in all_casino:
        for game_machine in casino.game_machines:
            if num_game_machine == counter:
                money = game_machine.money
                casino.game_machines.remove(game_machine)
                return money, casino
            counter += 1
