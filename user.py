from Incora_task.casino import Casino
from Incora_task.game_machine import print_all_available_game_mashine, delete_game_machine
from Incora_task.utils.cli import CLI


class User:
    # - конструктор приймає 2 вхідні параметри (name, money) -- ім'я і початкова сума грошей
    def __init__(self, name, money):
        self.name = name
        self.money = money

    # якщо грошей менше 0 - видаляємо користувача
    def check_money(self):
        if self.money == 0:
            print("!!!!!!!! ігра завершена, у Вас закінчились гроші !!!!!!!!!")
            CLI.work = False

    # play(money) -- почати гру за якимось GameMachine
    def start_game(self):
        if len(Casino.all_casino) == 0:
            print("Немає доступних казино")
            return
        Casino.print_available_casino()

        casino_number = int(input("Оберіть казино в якому бажаєте випробувати вдачу: ")) - 1
        money = int(input(f"Введіть суму яку бажаєте поставити в ігровий автомат, з можливих {self.money}: "))

        if money > self.money:
            print("У вас немає стільки грошей")
            return

        self.top_up_money(Casino.selection_game_mashine(self, casino_number, money))
        print("Ваш баланс", self.money)
        self.check_money()

    def reduce_money(self, money):
        self.money -= money

    def top_up_money(self, money):
        self.money += money


class SuperAdmin(User):
    def __init__(self, name, money):
        super(SuperAdmin, self).__init__(name, money)

    # створювати нове Казино
    def create_new_casino(self):
        name = str(input("Введіть назву казино: "))
        new_object = Casino(name)
        Casino.all_casino.append(new_object)

    # створювати ігрові автомати (GameMachine) у власному Casino (в цьому випадку новий автомат має
    # отримати стартову суму з грошей власника казино);
    def create_new_game_machine(self):
        if len(Casino.all_casino) == 0:
            print("Немає доступних казино")
            return

        Casino.print_available_casino()
        casino_number = int(input("Оберіть казино в яке бажаєте добавити в ігровий автомат: ")) - 1
        money = int(input("Введіть суму яку бажаєте виділити на ігровий автомат: "))

        Casino.add_game_machine_to_casino(self, casino_number, money)

    # - метод, щоб забрати з Casino гроші. Вхідний аргумент - сума (number). Вхідний аргумент - сума (number).
    # Функція має зібрати потрібну суму з автоматів (послідовність від автомата, у якому грошей найбільше, до
    # автомата у якому грошей найменше) і повернути її
    def get_money_from_casino(self):
        if len(Casino.all_casino) == 0:
            print("Немає доступних казино")
            return

        Casino.print_available_casino()

        casino_number = int(input("Оберіть казино з якого бажаєте зібрати гроші: ")) - 1
        required_money = int(input("Введіть потрібну суму: "))

        if casino_number > len(Casino.all_casino) + 1:
            print("Ви обрали неіснуюче казино")
            return

        money_from_casino = Casino.get_money_casino(casino_number, required_money)
        self.money += money_from_casino

    # - додавати гроші у Casino\Machine
    def add_money_to_machine(self):
        Casino.print_available_casino()
        casino_number = int(input("Оберіть казино куди бажаєте внести кошти: ")) - 1

        if casino_number > len(Casino.all_casino):
            print("Ви обрали неіснуюче казино")
            return

        print("Номер автомату  -- кошти")
        for index, machine in enumerate(Casino.all_casino[casino_number].game_machines):
            print(index, machine.money)

        number_machine = int(input("Виберіть автомат"))
        money = int(input(f"Виберіть суму з доступної, {self.money}"))
        if money > self.money:
            print("недостатньо коштів")
            return
        self.reduce_money(money)
        Casino.all_casino[casino_number].game_machines[number_machine].put_money(money)

    # - видалити ігровий автомат за номером (гроші з видаленого автомату розподіляються порівно між рештою автоматів
    # в даному казино)
    def delete_game_machine(self):

        print_all_available_game_mashine(Casino.all_casino)
        num_game_machine = int(input("Оберіть машину для видалення")) - 1

        money, casino = delete_game_machine(Casino.all_casino, num_game_machine)

        if casino.is_empty():
            self.money += money
        else:
            casino.division_funds(money)
