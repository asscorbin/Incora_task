from task_1.casino import Casino
from task_1.utils import config


class CLI:
    work = True

    def __init__(self, user, admin):
        self.admin = admin
        self.user = user

        self.using = True
        self.is_admin = True

        self.menu_user = {"1": user.start_game}

        self.menu_admin = {"1": Casino.create_new_casino,
                           "2": self.admin.create_new_game_machine,
                           "3": self.admin.get_money_from_casino,
                           "4": self.admin.add_money_to_machine,
                           "5": self.admin.delete_game_machine}

    def start(self):
        print(config.entering)

        while self.work:
            self.using = True

            if not self.is_admin:

                while self.using:
                    action = str(input(config.menu_user_text))
                    self.do_action(action, self.menu_user)

            elif self.is_admin:

                while self.using:
                    action = str(input(config.menu_admin_text))
                    self.do_action(action, self.menu_admin)
            else:
                oops()

    def do_action(self, action, menu):
        if action in menu.keys():
            menu[action]()

        elif action == "q":
            self.using = False
            self.is_admin = not self.is_admin

        elif action == "@":
            self.using = False
            self.work = False

        else:
            oops()


def oops():
    print("Упс, щось пішло не по плану...")
