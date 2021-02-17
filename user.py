from casino import Casino
from game_machine import GameMachine
from utils import config
from utils.cli import CLI


class User:
    # - конструктор приймає 2 вхідні параметри (name, money) -- ім'я і початкова сума грошей
    def __init__(self, name, money):
        self.name = name
        self.money = money

    # якщо грошей менше 0 - видаляємо користувача
    def check_money(self):
        if self.money == 0:
            print(config.user_bankruptcy)
            CLI.work = False

    # play(money) -- почати гру за якимось GameMachine
    def start_game(self):
        if Casino.is_empty_casino():
            print(config.empty_casino)
            return

        Casino.print_available_casino()

        casino_number = int(input(config.choose_casino_for_spin)) - 1

        self.print_balance()
        money = int(input(config.choose_money_for_spin))

        if not self.check_enough_money(money):
            print(config.user_has_not_enough_amount)
            return

        self.top_up_money(Casino.selection_game_mashine(self, casino_number, money))

        self.print_balance()

        self.check_money()

    def reduce_money(self, money):
        self.money -= money

    def top_up_money(self, money):
        self.money += money

    def get_money(self):
        return self.money

    def check_enough_money(self, money):
        return self.money >= money

    def print_balance(self):
        money = self.get_money()
        print(f"{config.print_balance} {money}")


class SuperAdmin(User):
    def __init__(self, name, money):
        super(SuperAdmin, self).__init__(name, money)

    # створювати ігрові автомати (GameMachine) у власному Casino (в цьому випадку новий автомат має
    # отримати стартову суму з грошей власника казино);
    def create_new_game_machine(self):
        if Casino.is_empty_casino():
            print(config.empty_casino)
            return

        Casino.print_available_casino()

        casino_number = int(input(config.choose_casino_for_add_machine)) - 1

        if Casino.check_available_casino(casino_number):
            print(config.empty_name_casino)
            return

        self.print_balance()
        money = int(input(config.choose_amount_money_for_add__machine))

        if not self.check_enough_money(money):
            print(config.user_has_not_enough_amount)
            return

        GameMachine.add_game_machine(self, casino_number, money)

    # - метод, щоб забрати з Casino гроші. Вхідний аргумент - сума (number). Вхідний аргумент - сума (number).
    # Функція має зібрати потрібну суму з автоматів (послідовність від автомата, у якому грошей найбільше, до
    # автомата у якому грошей найменше) і повернути її
    def get_money_from_casino(self):
        if Casino.is_empty_casino():
            print(config.empty_casino)
            return

        Casino.print_available_casino()

        casino_number = int(input(config.choose_casino_for_take_money)) - 1

        if Casino.check_available_casino(casino_number):
            print(config.empty_name_casino)
            return

        required_money = int(input(config.enter_necessary_amount))

        available_money = GameMachine.get_money()

        if required_money > available_money:
            print(config.game_machines_have_not_enough_money)
            return

        money_from_casino = Casino.get_money_casino(casino_number, required_money)
        self.top_up_money(money_from_casino)

        self.print_balance()

    # - додавати гроші у Casino\Machine
    def add_money_to_machine(self):
        if Casino.is_empty_casino():
            print(config.empty_casino)
            return

        Casino.print_available_casino()

        casino_number = int(input(config.choose_casino_for_add_money)) - 1

        if Casino.check_available_casino(casino_number):
            print(config.empty_name_casino)
            return

        print(config.print_game_machine_info)
        for index, machine in enumerate(Casino.all_casino[casino_number].game_machines):
            print(index + 1, machine.money)

        num_game_machine = int(input(config.choose_game_machine)) - 1

        if GameMachine.check_available_game_machine(num_game_machine):
            print(config.empty_name_game_machine)
            return

        self.print_balance()
        money = int(input(config.enter_necessary_amount))

        if not self.check_enough_money(money):
            print(config.user_has_not_enough_amount)
            return

        self.reduce_money(money)
        Casino.all_casino[casino_number].game_machines[num_game_machine].put_money(money)

    # - видалити ігровий автомат за номером (гроші з видаленого автомату розподіляються порівно між рештою автоматів
    # в даному казино)
    def delete_game_machine(self):
        if GameMachine.is_empty_game_machine():
            print(config.empty_game_machine)
            return

        GameMachine.print_all_available_game_machine()
        num_game_machine = int(input(config.choose_game_machine_for_delete)) - 1

        if GameMachine.check_available_game_machine(num_game_machine):
            print(config.empty_name_game_machine)
            return

        num_casino = Casino.get_number_casino_from_game_machine(num_game_machine)
        money, casino = GameMachine.delete_game_machine(num_game_machine)

        if Casino.is_empty_game_machine_in_casino(num_casino):
            self.top_up_money(money)
            Casino.all_casino.pop(num_casino)
        else:
            casino.division_funds(money)
