from user import User, SuperAdmin
from utils.cli import CLI

if __name__ == '__main__':
    user = User("Олег", 100)
    admin = SuperAdmin("Олег", 100)

    cli = CLI(user, admin)
    cli.start()
