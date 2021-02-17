from utils import config


class Casino:
    all_casino = []

    # - Конструктор класу Casino приймає один параметр (name) - назва казино
    def __init__(self, name):
        self.name_casino = name
        self.game_machines = []

    # - геттер getMoney - отримати загальну суму грошей у Casino
    def get_total_money(self):
        return sum([int(machine.money) for machine in self.game_machines])

    # - геттер getMachineCount - отримати кількість автоматів у Casino
    def get_machine_count(self):
        return len(self.game_machines)

    def division_funds(self, money):
        count_machine = self.get_machine_count()

        money_for_machine = money // count_machine

        for machine in self.game_machines:
            machine.money += money_for_machine

        remainder = money % count_machine
        if remainder > 0:
            for i in range(remainder):
                self.game_machines[i].money += 1

    def is_empty_game_machine(self):
        return len(self.game_machines) == 0

    # створювати нове Казино
    @classmethod
    def create_new_casino(cls):
        name = str(input(config.enter_name_casino))
        new_object = Casino(name)
        cls.all_casino.append(new_object)

    @staticmethod
    def selection_game_mashine(user, casino_number, money):
        if Casino.all_casino[casino_number] in Casino.all_casino:
            for game_machine in Casino.all_casino[casino_number].game_machines:
                if game_machine.check_enough_money(money):
                    user.reduce_money(money)
                    return game_machine.spin(money)
                else:
                    return 0

            print(config.empty_enough_money_at_game_machine)
            return 0

    @staticmethod
    def get_money_casino(casino_number, required_money):
        money_from_casino = 0

        game_machines = Casino.all_casino[casino_number].game_machines
        sorted_game_machines = sorted(game_machines, key=lambda machine: machine.money, reverse=True)

        for game_machine in sorted_game_machines:

            if money_from_casino + game_machine.money > required_money:

                fraction = required_money - (money_from_casino + game_machine.money)
                money_from_casino = game_machine.money - fraction
                game_machine.money = -fraction
                return money_from_casino
            elif money_from_casino + game_machine.money == required_money:

                money_from_casino = game_machine.money
                if game_machine in Casino.all_casino[casino_number].game_machines:
                    Casino.all_casino[casino_number].game_machines.remove(game_machine)
                return money_from_casino

            money_from_casino += game_machine.money
            game_machine.money = 0
            if game_machine in Casino.all_casino[casino_number].game_machines:
                Casino.all_casino[casino_number].game_machines.remove(game_machine)

    @classmethod
    def print_available_casino(cls):
        print(config.list_of_available_casino)

        for i in range(len(cls.all_casino)):
            print(f' * {i + 1} \t\t {cls.all_casino[i].name_casino}')

    @classmethod
    def is_empty_casino(cls):
        return not cls.all_casino

    @classmethod
    def check_available_casino(cls, number):
        return not cls.all_casino[number] in cls.all_casino

    @staticmethod
    def get_number_casino_from_game_machine(number):
        counter = 0
        num_casino = 0
        for casino in Casino.all_casino:
            for game_machine in casino.game_machines:
                if counter == number:
                    return num_casino
                counter += 1
            num_casino += 1

    @classmethod
    def is_empty_game_machine_in_casino(cls, num_casino):
        return Casino.all_casino[num_casino].game_machines == 0
