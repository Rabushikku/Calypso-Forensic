from functions import menu

def prompt(menus, upper=False):
    menu.clear_console()
    menus()
    answer = input('-> ').strip()
    return answer.upper() if upper else answer

def legal_setup():
    try:
        while True:
            case_number = prompt(menu.case_number_menu)
            crime_type = prompt(menu.crime_type_menu)
            confirm = prompt(menu.warning_screen, upper=True)
            
            if confirm == 'N':
                menu.system_exit()
                return
            
            if confirm != 'Y':
                continue
            
    except KeyboardInterrupt:
        menu.system_exit()