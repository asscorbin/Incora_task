from utils import config


# CLI --> Command Line Interface
class CLI:
    work = True

    def __init__(self, user, admin):
        self.admin = admin
        self.user = user

        self.using = True

        self.menu_user = {"1": user.start_game}

        self.menu_admin = {"1": self.admin.create_new_casino,
                           "2": self.admin.create_new_game_machine,
                           "3": self.admin.get_money_from_casino,
                           "4": self.admin.add_money_to_machine,
                           "5": self.admin.delete_game_machine}

    def start(self):
        print("\n\t____ Вітаю Вас в казино ____"
              "\n\t**** Оберіть тип користувача ****            (для звершення роботи використовуйте '@'")

        self.type_user = int(input("\t0 - Користувач \n\t1 - Власник\n Зробіть свій вибір: "))

        while self.work:
            self.using = True

            if self.type_user == 0:

                while self.using:
                    action = str(input(config.menu_user_text))
                    self.do_action(action, self.menu_user)

            elif self.type_user == 1:

                while self.using:
                    action = str(input(config.menu_admin_text))
                    self.do_action(action, self.menu_admin)
            else:
                oops()

    def do_action(self, action, menu):
        if action in menu.keys():
            menu[action]()
        elif action == "q":
            print("Міняємо користувача")
            self.using = False
            self.type_user += 1
            self.type_user %= 2
        elif action == "@":
            self.work = False
        else:
            oops()


def oops():
    print("Упс, щось пішло не по плану...")
