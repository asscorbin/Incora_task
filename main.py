from Incora_task.user import User, SuperAdmin
from Incora_task.utils.cli import CLI

if __name__ == '__main__':
    user = User("Олег", 100)
    admin = SuperAdmin("Олег", 100)

    cli = CLI(user, admin)
    cli.start()
