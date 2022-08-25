import random
import colorama
from colorama import Fore, Back, Style
colorama.init()
import time

print("""\
    
██████╗░██╗░░░██╗░█████╗░░██████╗
██╔══██╗╚██╗░██╔╝██╔══██╗██╔════╝
██████╔╝░╚████╔╝░██║░░██║╚█████╗░
██╔═══╝░░░╚██╔╝░░██║░░██║░╚═══██╗
██║░░░░░░░░██║░░░╚█████╔╝██████╔╝
╚═╝░░░░░░░░╚═╝░░░░╚════╝░╚═════╝░
""")

def home():
    print("What do you wanna do today?")
    print(Fore.GREEN + "1. Calculator\n2. Random Joke\n3. About PyOS\n 4. Guess The Word\n 5. Power Options\n6. Save Code")
    home_option = input("Choose your option. ")
    if home_option == "6":
        print("Your savecode is: PyOS2022HomeUserWIP")
        time.sleep(1)
        print("Save codes are to login without setting up your PC once again.") 

    elif home_option == "5":
        print("1. Power Off\n2. Restart your PC\n3. Log Out")
        power_option = input("Choose your option. ")
        while power_option != "1" or power_option != "2" or power_option != "3" or power_option != "back" or power_option != "Back":
            print(Fore.RED + "Invalid Option. ")
            power_option = input("Choose your option. ")
            if power_option == "1":
                print("Shutting down...")
                time.sleep(2)
                exit()
            elif power_option == "2":
                print("Restarting your PC...")
                time.sleep(1)
                print(Fore.RED + "Error Occured while restarting your PC. Please try again later.")
                exit()
            elif power_option == "3":
                print(Fore.RED + "Logging out.")
                exit()
        
            elif power_option == "back" or power_option == "Back":
                home()
        if power_option == "1":
            print(Fore.GREEN + "Powering off your PC.")
            time.sleep(2)
            exit()
        
        elif power_option == "2":
            print(Fore.RED + "Restarting your PC..")
            time.sleep(2)
            print("Error occured while trying to restart your device. Please try again later.")
            exit()
         
        elif power_option == "3":
            print("Logging out..")
            time.sleep(3.5)
            exit()
        
        elif power_option == "back" or power_option == "Back":
            home()

    elif home_option == "4":
        print(Fore.RED + "Coming Soon!")
        time.sleep(2.3)
        home()
    
    elif home_option == "3":


        print(Fore.GREEN + "PyOS, built and programmer by PrimeDev#7041, is the first version ever built by him.\n Even though it isn't much, it is highly\ninspired by Microsoft Windows.\n More versions of PyOS will come.\n")
        home()

    elif home_option == "2":
        pass

def setup():
    print(Fore.GREEN + "Let's finish setting up your PC. ")
    print(Fore.YELLOW + "Is this the right country or region?\n1. United States")
    select_country = input("Select your country by typing the number of it. ")
    while select_country != "1" or select_country != "2":
        print(Fore.RED + "Dang, looks like something went wrong! A mysterious island has appeared, we're gonna check it out.")
        select_country = input("Select your country by typing the number of it. ")
        if select_country == "1":
            break
    print(Fore.GREEN + "Let's name your PC.")
    pc_name = input(Fore.BLUE + "Name your PC. ")
    name_pc = open("pcname.txt", "w")
    name_pc.write(pc_name)
    name_pc.close()
    confirm_pc_name = input(Fore.GREEN + "Confirm your PC name. ")
    read_pc_name = open("pcname.txt", "r")
    read_namepc = read_pc_name.readline()

    while confirm_pc_name != read_namepc:
        print(Fore.RED + "Hm, that didn't quite match your PC's name. Please try again.")
        time.sleep(2)
        confirm_pc_name = input(Fore.GREEN + "Confirm your PC name. ")
        if confirm_pc_name == read_namepc:
            break
    
    if confirm_pc_name == read_namepc:
        print(Fore.YELLOW + "Name set to your PC.")
    time.sleep(1)
    print(Fore.YELLOW + """\
        𝗛𝗼𝘄 𝘄𝗶𝗹𝗹 𝘆𝗼𝘂 𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝗱𝗲𝘃𝗶𝗰𝗲❓
        """)
    choose_how = input(Fore.GREEN + "1. For Personal Use\n2. For Work or School\nChoose your option. ")
    while choose_how != "1" or choose_how != "2":
        print(Fore.RED + "Invalid Option.")
        choose_how = input(Fore.GREEN + "1. For Personal Use\n2. For Work or School\nChoose your option. ")
        if choose_how == "1" or choose_how == "2":
            break
    if choose_how == "1" or choose_how == "2":
        print("Option set.")
    
    time.sleep(2)
    print(Fore.GREEN + """\
                        𝗪𝗲❜𝗿𝗲 𝘀𝗲𝘁𝘁𝗶𝗻𝗴 𝘂𝗽 𝘆𝗼𝘂𝗿 𝗣𝗖.
           𝗧𝗵𝗶𝘀 𝗺𝗶𝗴𝗵𝘁 𝘁𝗮𝗸𝗲 𝗮 𝗳𝗲𝘄 𝗺𝗶𝗻𝘂𝘁𝗲𝘀, 𝗱𝗼𝗻𝘁 𝘁𝘂𝗿𝗻 𝗼𝗳𝗳 𝘆𝗼𝘂𝗿 𝗣𝗖.
           """)
    time.sleep(6.5)
    home()
    

    
    




def begin():

    welcome = input(Fore.GREEN + "Welcome to PyOS. To begin type Create, create, login, or Login. : ")
    while welcome != "login" or welcome != "Login" or welcome != "Create" or welcome != "create" or welcome == "PyOS2022HomeUserWIP":
        print(Fore.RED + "Invalid option. ")
        welcome = input(Fore.GREEN + "Welcome to PyOS. To begin type Create, create, login, or Login. ")
        if welcome == "login" or welcome == "Login" or welcome == "create" or welcome == "Create" or welcome == "PyOS2022HomeUserWIP":
            break
    if welcome == "info" or welcome == "Info":


        print("1. Create Account\n2. Login Now\n\n")
        infohelp = input("Choose your option by typing an number. ")
        while infohelp != "1" or infohelp != "2":
            print(Fore.RED + "Unable to find option. Please enter an valid option above. ")
            infohelp = input("Choose your option by typing an number. ")
            if infohelp == "1":
                print(Fore.GREEN + "Type Create or create to make an account. Restart the OS now to begin again.")
                exit()
            elif infohelp == "2":
                print(Fore.GREEN + "Type Login or login when restarting the program to login into your account. Please re-run the program now to begin.")
                exit()

    elif welcome == "create" or welcome == "Create":
        print(Fore.YELLOW + "Let's get to know each other.")
        createacc = input("Enter a username: ")
        print(Fore.RED + "Enter a password that you can remember. ")
        createpass = input("Enter a password: ")
        time.sleep(1)
        print(Fore.YELLOW + "Alright, now we're gonna need your email if you lose your password.")
        emailcreate = input("Enter your email: ")
        file = open("username.txt", "w")
        file.write(createacc)
        file.close()
        file2 = open("password.txt", "w")
        file2.write(createpass)
        file2.close()
        file3 = open("email.txt", "w")
        file3.write(emailcreate)
        file3.close()
        time.sleep(2)
        print("Alright! You're set.")
        time.sleep(1)
        print("We're restarting your PC and collecting some info. Please wait.")
        waits = ["Please wait.", "Please Wait..", "Please wait..."]
        loadingwelcome = random.choice(waits)
        for i in range(3):
            print(loadingwelcome)
            time.sleep(1)
        begin()

    elif welcome == "login" or welcome == "Login":
        login = input("Enter username: ")
        readuser = open("username.txt", "r")
        readloginuser = readuser.readline()
        while login != readloginuser:
            print(Fore.RED + "Oh noes! Looks like that user doesn't exist. To recover your account, type your email.")
            login = input(Fore.YELLOW + "Enter username: ")
            if login == readloginuser:
                break
            reademail = open("email.txt", "r")
            reademaillogin = reademail.readline()
            if login == reademaillogin:
                print(Fore.GREEN + "1 second..")
                time.sleep(1)
                print(readloginuser)
        login2 = input(Fore.YELLOW + "Enter password: ")
        readpass = open("password.txt", "r")
        readpasslogin = readpass.readline()
        while login2 != readpasslogin:
            print(Fore.RED + "Wrong username or Password. Please try again.")
            login2 = input(Fore.YELLOW + "Enter password: ")
            if login2 == readpasslogin:
                print(Fore.YELLOW + "Welcome to PyOS!")
                setup()
                break
        if login2 == readpasslogin:
            print(Fore.GREEN + "Welcome to PyOS!!")
            setup()
    
    elif welcome == "PyOS2022HomeUserWIP":
        home()
    

begin()
    
