from game_machine import GameMachine


# from utils.cli import oops


class Casino:
    all_casino = []

    # - Конструктор класу Casino приймає один параметр (name) - назва казино
    def __init__(self, name):
        self.name_casino = name
        self.game_machines = []

    # - геттер getMoney - отримати загальну суму грошей у Casino
    def get_total_money(self):
        total = sum([int(machine.money) for machine in self.game_machines])
        return total

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

    def is_empty(self):
        return len(self.game_machines) == 0


    @staticmethod
    def selection_game_mashine(user, casino_number, money):
        if Casino.all_casino[casino_number] in Casino.all_casino:
            for game_machine in Casino.all_casino[casino_number].game_machines:
                if game_machine.check_enough_money(money):
                    user.reduce_money(money)
                    return game_machine.spin(money)
                else:
                    return 0

            print("!!! Автомат для роботи з такою сумою відсутній !!!"
                  "\n зверніться до адміністратора щоб він поповнив їх або ж спробуйте зіграти в іншому казино")
        # else:
        #     oops()

    @staticmethod
    def add_game_machine_to_casino(user, casino_number, money):
        if casino_number in range(len(Casino.all_casino)):
            user.reduce_money(money)
            new_game_machine = GameMachine(money)
            Casino.all_casino[casino_number].game_machines.append(new_game_machine)
        # else:
        #     oops()

    @staticmethod
    def get_money_casino(casino_number, required_money):
        money_from_casino = 0
        if Casino.all_casino[casino_number] in Casino.all_casino:
            print("Казино типу вибрали")
            if required_money <= Casino.all_casino[casino_number].get_total_money():
                print("Грошей хватає")

                game_machines = Casino.all_casino[casino_number].game_machines

                sorted_game_machines = sorted(game_machines, key=lambda machine: machine.money, reverse=True)

                print("Виводимо 1 раз усі автомати")
                for i in sorted_game_machines:
                    print(i.money)

                for game_mashine in sorted_game_machines:
                    print("Проходимось по автоматах")

                    if money_from_casino + game_mashine.money > required_money:
                        print("це щяс ми на кінцевому")
                        print(required_money, "- (", money_from_casino, "+", game_mashine.money, ")")
                        fraction = required_money - (money_from_casino + game_mashine.money)
                        print("Остача", fraction)
                        print(money_from_casino, "=", game_mashine.money, "-", fraction)
                        money_from_casino = game_mashine.money - fraction
                        print("money_from_casino", money_from_casino)
                        game_mashine.money = -fraction
                        print("game_mashine.money", game_mashine.money)

                        for i in sorted_game_machines:
                            print(i.money)

                        return money_from_casino
                    elif money_from_casino + game_mashine.money == required_money:
                        print("Воно в притик")
                        money_from_casino = game_mashine.money
                        if game_mashine in Casino.all_casino[casino_number].game_machines:
                            Casino.all_casino[casino_number].game_machines.remove(game_mashine)

                            for i in sorted_game_machines:
                                print(i.money)

                        return money_from_casino

                    print("Добавили бабки")
                    money_from_casino += game_mashine.money
                    game_mashine.money = 0
                    if game_mashine in Casino.all_casino[casino_number].game_machines:
                        Casino.all_casino[casino_number].game_machines.remove(game_mashine)
            else:
                print("в казино недостатьо коштів")

    @staticmethod
    def print_available_casino():
        print("Список доступних казино:")

        for i in range(len(Casino.all_casino)):
            print(f' * {i + 1} \t\t {Casino.all_casino[i].name_casino}')
