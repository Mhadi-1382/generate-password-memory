'''
Generate Password Memory is an app to create very strong passwords and
also the storage of all the passwords that is,
it's good because you are no longer worried
about forgetting your passwords.

See Code Github: https://github.com/Mhadi-1382/
'''

import sqlite3
import random
import string
import colorama
import os
import datetime


connectdb = sqlite3.connect("password_database.db")
cursor = connectdb.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS passwordMemory (
        Password TEXT,
        CreatedDate DATE
    );
''')


def splash_screen():
    """Splash screen"""

    os.system("cls")
    
    splash_printer = """
    ------------------------------------------------
    -- G E N E R A T E  P A S S W O R D  M E M O R Y
    ------------------------------------------------
    __ MADE: MOHAMMAD MAHDI RABIEE __
    __ GITHUB: https://github.com/Mhadi-1382/ __

    [0] - Generate Password
    [1] - Show Generated Passwords
    [2] - Delete Generated Passwords
    [3] - Exit

    Choose Options:
    """
    print(colorama.Fore.RED + splash_printer + colorama.Fore.WHITE)

splash_screen()


def prompt():
    """Prompt or get commands"""

    prompt_get_user = int(input(":: "))

    if prompt_get_user == 0:
        generate_password()
    elif prompt_get_user == 1:
        show_password()
        print()
    elif prompt_get_user == 2:
        delete_password()
    elif prompt_get_user == 3:
        connectdb.close()
        exit()
    else:
        print(colorama.Fore.YELLOW + "[!] INVALID." + colorama.Fore.WHITE + "\n")
        prompt()


def generate_password():
    """Generate password"""

    alpha = string.ascii_letters
    symbol = string.punctuation
    numbers = string.digits
    set_char = alpha + symbol + numbers

    while True:
        len_password = input("LEN PASSWORD: ")

        result = "".join(random.sample(set_char, int(len_password)))
        print(result + "\n")

        result_send_database = (f'{result}', f'{datetime.datetime.now()}',)
        cursor.execute('''
            INSERT INTO passwordMemory VALUES(?,?);
        ''', result_send_database)
        connectdb.commit()


def delete_password():
    """Delete passwords"""

    cursor.execute('''
        DROP TABLE passwordMemory;
    ''')
    connectdb.commit()
    print(colorama.Fore.GREEN + "[+] PASSWORD HAVE BEEN SUCCESSFULLY DELRTED." + colorama.Fore.WHITE + "\n")


def show_password():
    """Show passwords"""

    cursor.execute('''
        SELECT * FROM passwordMemory;
    ''')
    show_all_password = cursor.fetchall()
    for passwords in show_all_password:
        print(passwords)

    if show_all_password == []:
        print(colorama.Fore.YELLOW + "[-] PASSWORD HAS NOT BEEN SAVED." + colorama.Fore.WHITE)

prompt()
