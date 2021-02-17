import random

from casino import Casino
from utils import config


class GameMachine:

    # - Конструктор класу приймає один вхідний параметр: початкову суму грошей яка заноситься в автомат (number)
    def __init__(self, money):
        self.money = money

    # - геттер getMoney - отримати загальну суму грошей у GameMachine
    @staticmethod
    def get_money():
        total_money_game_machine = 0
        for casino in Casino.all_casino:
            for game_machine in casino.game_machines:
                total_money_game_machine += game_machine.money
        return total_money_game_machine

    # - метод, щоб забрати з GameMachine гроші. Вхідний аргумент - сума (number)
    def take_money(self, money):
        self.money -= money
        return self.money

    # - Покласти гроші. Вхідний аргумент - сума (number)
    def put_money(self, money):
        self.money += money

    # - Зіграти. Вхідний аргумент - сума (number) грошей, яку гравець закидує в автомат.
    def spin(self, money):
        self.put_money(money)

        # Генеруємо випадково 3-х значне число
        generated_number = str(random.randint(0, 999)).rjust(3, '0')
        print(generated_number)

        # Якщо 3 цифри однакові - повертається 3-кратна сума
        if generated_number.count(i) == 3:
            print(f"{config.win_x3} {generated_number}")
            return money * 3

        for i in generated_number:
            if generated_number.count(i) == 2:
                print(f"{config.win_x2} {generated_number}")
                return money * 2

        print(f"{config.lose} {generated_number}")
        return 0

    def check_enough_money(self, money):
        return self.money >= int(money) * 3

    @classmethod
    def print_all_available_game_machine(cls):
        print(config.print_all_game_machine_info)
        counter = 0
        for casino in Casino.all_casino:
            for game_machine in casino.game_machines:
                counter += 1
                print(f"\t  {counter}\t\t{game_machine.money}")

    @classmethod
    def delete_game_machine(cls, num_game_machine):
        counter = 0
        for casino in Casino.all_casino:
            for game_machine in casino.game_machines:
                if num_game_machine == counter:
                    money = game_machine.money
                    casino.game_machines.remove(game_machine)
                    return money, casino
                counter += 1

    @staticmethod
    def add_game_machine(user, casino_number, money):
        if casino_number in range(len(Casino.all_casino)):
            user.reduce_money(money)
            new_game_machine = GameMachine(money)
            Casino.all_casino[casino_number].game_machines.append(new_game_machine)

    @staticmethod
    def is_empty_game_machine():
        count = GameMachine.get_count_game_machines
        return count == 0

    @classmethod
    def check_available_game_machine(cls, number_machine):
        count = GameMachine.get_count_game_machines()
        return number_machine >= count

    @staticmethod
    def get_count_game_machines():
        count = 0
        for casino in Casino.all_casino:
            count += len(casino.game_machines)

        return count
