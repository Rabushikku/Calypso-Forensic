from functions import menu

def start_extraction():
    try:
        menu.clear_console()
        
        menu.asciiart()
        
    except KeyboardInterrupt:
        pass
        