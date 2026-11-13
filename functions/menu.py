from rich.console import Console
import pyfiglet
import sys
import os
import time
from tqdm import tqdm

console = Console()
CRIME_LIST = {
    '1':  'Border security assessments',
    '2':  'Civil Case or investigation',
    '3':  'Corruption', 
    '4':  'Child exploitation',
    '5':  'Data exfiltration / IP theft',
    '6':  'Drug Offenses',
    '7':  'Fraud',
    '8':  'HR / internal investigation',
    '9':  'Human trafficking',
    '10': 'intrusion / incident response',
    '11': 'Major Crimes (murder, drug trafficking, weapons trafficking)',
    '12': 'Military investigation',
    '13': 'Organized crime',
    '14': 'Policy violation',
    '15': 'Probation / parole violation',
    '16': 'Terrorism',
    '17': 'Other',
}

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def system_exit():
    sys.exit(0)
    
def asciiart():
    banner = pyfiglet.figlet_format(
        'Calypso', 
        font='double_shorts'
        )
    
    lines = banner.split('\n')
    
    width = max(len(line) for line in lines)
    padding = (console.width - width) // 2
    centered = ' \n'.join(' ' * padding + line for line in lines)
    full_banner = f'[#1ebbd7]{centered}[/#1ebbd7]'
    
    console.print(full_banner)

def main_options():
    console.print(
        '[#1ebbd7]»1« Start Data Extraction  »2« Exit[/#1ebbd7]', 
        justify='center'
    )
    
def warning_screen():
    clear_console()
    
    console.print(
        'Are you sure you want to start the extraction?\n Y = Yes | N = No',
        justify='center',
        style='red'
    )
    
def case_number_menu():
    clear_console()
    
    asciiart()
    console.print(
        '[#1ebbd7]Enter Case Number[/#1ebbd7]',
        justify='center'
    )
    
def crime_type_menu():
    clear_console()
    
    console.print(
        '[#1ebbd7]Enter crime type.[/#1ebbd7]',
        justify='center'
    )
    for number, crime in CRIME_LIST.items():
        print(number, crime)     
        
def progress_bar():
    for i in tqdm(range(100), desc="Extracting"):
        time.sleep(0.05)