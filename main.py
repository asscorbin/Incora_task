from utils.cli import CLI
from user import User, SuperAdmin

if __name__ == '__main__':
    user = User("Олег", 100)
    admin = SuperAdmin("Олег", 100)

    cli = CLI(user, admin)
    cli.start()
