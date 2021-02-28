start_menu = "\n\t**** Оберіть дію ****"
nav_menu = "\n q - змінити корситувача" \
           "\n @ - завершити роботу програми" \
           "\n Введіть номер потрібної вам дії :"

menu_user_text = start_menu + "\n 1 - зіграти" + nav_menu

menu_admin_text = start_menu + "\n 1 - Створити казино" \
                               "\n 2 - Створити автомат" \
                               "\n 3 - Забрати гроші з казино" \
                               "\n 4 - Добавити гроші у Казино/Автомат" \
                               "\n 5 - Видалити автомат" + nav_menu

# _______________ print errors ________________________________________________________________
empty_casino = "!!!! Ще не були створені казино !!!!"
empty_name_casino = "!!!! Ви обрали неіснуюче казино !!!!"
empty_name_game_machine = "!!!! Ви обрали неіснуючий ігровий автомат !!!!"
user_bankruptcy = "!!!! упс, закінчились гроші !!!!"
empty_game_machine = "!!!! Ще не були створені ігрові автомати !!!!"
empty_enough_money_at_game_machine = "!!! Автомат для роботи з такою сумою відсутній !!!"
game_machines_have_not_enough_money = "В ігрових автоматах зе не назбиралось стільки грошей"

# ________________ work with casino ________________________________________________________________
enter_name_casino = "Введіть назву казино: "
list_of_available_casino = "Список доступних казино:"
# __________________ user ________________________________________________________________
entering = "\t\t *** Вітаю Вас в казино ***"
available_money = "Кошти доступні Вам для користування - "
enter_necessary_amount = "Введіть необхідну суму"
user_has_not_enough_amount = "У вас немає стільки грошей"
print_balance = "На вашому балансі"

choose_casino_for_spin = "Оберіть казино в якому бажаєте випробувати вдачу: "
choose_money_for_spin = "Введіть суму яку бажаєте поставити в ігровий автомат :"

guess_number = "\n\n\t Загадане число: "
win_x2 = "МОї вітання, х2" + guess_number
win_x3 = "МОї вітання, х3" + guess_number
lose = "Ви програли" + guess_number

choose_casino_for_take_money = "Оберіть казино з якого бажаєте зібрати гроші: "
choose_casino_for_add_machine = "Оберіть казино в яке бажаєте добавити в ігровий автомат: "
choose_amount_money_for_add__machine = "Введіть суму яку бажаєте виділити на ігровий автомат: "

choose_casino_for_add_money = "Оберіть казино куди бажаєте внести кошти: "
choose_game_machine = "Виберіть автомат"
choose_game_machine_for_delete = "Оберіть машину для видалення"
# ____________________ game machine ________________________________________________________________
print_game_machine_info = "Номер автомату  -- кошти"
print_all_game_machine_info = "Усі наявні ігрові автомати :\n" + print_game_machine_info
