from functions import menu
import legal_page

def main():
    user_options = {
        '1': legal_page.legal_setup,
        '2': lambda: menu.system_exit
    }
    
    try:
        while True:
            menu.clear_console()
            menu.asciiart()
            menu.main_options()
            
            userinput = input('-> ')
            actions = user_options.get(userinput)
            
            if actions: 
                actions()
            else:
                pass
    
    except KeyboardInterrupt:
        menu.system_exit()

if __name__ == '__main__':
    main()