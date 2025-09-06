import sys
import time
from time import sleep, strftime
from datetime import datetime
import threading
import webbrowser, os, re, json, random
import msvcrt
import subprocess
import ctypes
try:
    from faker import Faker
    from requests import session
    from colorama import Fore, Style
    import requests
    from random import choice, randint, shuffle
    import pystyle
    from pystyle import Add, Center, Anime, Colors, Colorate, Write, System, Box
except:
    os.system("pip install faker")
    os.system("pip install requests")
    os.system("pip install colorama")
    os.system('pip install requests && pip install bs4 && pip install pystyle && pip install pycryptodome')

def windowtitle(a):
    os.system(f"title {a}")

windowtitle("MCC Loader 1.1.0")

xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
whiteb = "\033[1;39m"
red = "\033[0;31m"
redb = "\033[1;31m"
end = '\033[0m'
dev = "\033[1;39m[\033[1;31m×\033[1;39m]\033[1;39m"

f = os.path.expanduser(r'~\AppData\Roaming\MCCFree\MCCTOS\TOSVDOIAHWOIHSAKLFHWA.txt')

TOS = """




                                               \033[0;31m _       _____    __________
                                               \033[0;31m| |     / /   |  /  _/_  __/
                                               \033[0;31m| | /| / / /| |  / /  / /   
                                               \033[0;31m| |/ |/ / ___ |_/ /  / /    
                                               \033[0;31m|__/|__/_/  |_/___/ /_(_)
"""
TOS2 = """                  Before using MCC Loader, you must agree to our \033[0;31mTOS\033[1;39m.
                                    
              Only press enter if you want to see the \033[0;31mterms of service\033[1;39m."""

TOS_content = """
              The term "We" refers to the entire Developer/Owner of MCC's Archive and MCC's Archive as a whole, 
                   while "You" refers to you as the user and person using the products of MCC's Archive.

     You need to ensure that you voluntarily download/use MCC Loader without any coercion from anyone/a third party.
  "Someone/a third party" here mainly refers to the cases You are asked by a server/stranger to start this application.

            By pressing continue(enter), you agree that you will not use MCC Loader in particular/MCC's Archive
                                products in general for commercial purposes(eg selling).

             You must also accept that you will be solely responsible for all situations/cases that MAY occur
               to your device during/after the period of using the PRODUCTS IN MCC Loader. (Not the loader.)

            At the same time, we will maintain and ensure the safety of all users when using MCC Loader and any 
 participation/influence on our actions may result in a PERMANENT BAN OF HWID of the person who committed the above act.

            By continuing to use any products maintained by MCC's Archive, you voluntarily agree to be bound 
                                by the most current version of the Terms of Service.
"""

def confirm():
    Anime.Fade(Center.Center(TOS2), Colors.white_to_red, Colorate.Vertical, enter=True)

try:
    with open(f, 'r') as file:
        pass
except FileNotFoundError:
    os.system('cls')
    print(TOS)
    time.sleep(1)
    print("\033[1;39m[\033[0;31mMCC Loader\033[1;39m] \033[1;39mThe user haven't accepted MCC Loader's terms of service.")
    time.sleep(1)
    print("\033[1;39m[\033[0;31mMCC Loader\033[1;39m] \033[1;39mRedirect user to : \033[0;31mTOSArea.")
    time.sleep(3)
    os.system('cls')
    print(TOS2) 
    confirm()
    os.system('cls')
    print("\033[1;31m                                Press any key only when you agree and understand the TOS.")
    print(Box.Lines("MCC's Archive Terms of Service (TOS)"))
    Write.Print(TOS_content, Colors.white_to_green, interval=0.00025)
    msvcrt.getch()
    os.makedirs(os.path.dirname(f), exist_ok=True)
    with open(f, 'a') as file:
        file.write("The user accepted MCC's Archive's terms of service.\n")
else:
    with open(f, 'a') as file:
        file.write("\nUser accepted the terms.")

banner = """
                                      You have accepted MCC Loader's terms of service.

                 ███╗░░░███╗░█████╗░░█████╗░██╗░██████╗  ░█████╗░██████╗░░█████╗░██╗░░██╗██╗██╗░░░██╗███████╗
                 ████╗░████║██╔══██╗██╔══██╗╚█║██╔════╝  ██╔══██╗██╔══██╗██╔══██╗██║░░██║██║██║░░░██║██╔════╝
                 ██╔████╔██║██║░░╚═╝██║░░╚═╝░╚╝╚█████╗░  ███████║██████╔╝██║░░╚═╝███████║██║╚██╗░██╔╝█████╗░░
                 ██║╚██╔╝██║██║░░██╗██║░░██╗░░░░╚═══██╗  ██╔══██║██╔══██╗██║░░██╗██╔══██║██║░╚████╔╝░██╔══╝░░
                 ██║░╚═╝░██║╚█████╔╝╚█████╔╝░░░██████╔╝  ██║░░██║██║░░██║╚█████╔╝██║░░██║██║░░╚██╔╝░░███████╗
                 ╚═╝░░░░░╚═╝░╚════╝░░╚════╝░░░░╚═════╝░  ╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚══════╝

                                                 Press ENTER to continue.                                                                     
"""
Anime.Fade(Center.Center(banner), Colors.black_to_white, Colorate.Vertical, enter=True)

nig = """
                                                  \033[1;39mMCC Loader is FREE.

                \033[1;32m\033[1;39mWhat's new in MCC Loader 1.1.0? Checkout new feature & cheats here: discord.gg/chiterl


                          \033[1;36m______  ___________________   ______              _________            
                          \033[1;36m___   |/  /_  ____/_  ____/   ___  / ____________ ______  /____________
                          \033[1;36m__  /|_/ /_  /    _  /        __  /  _  __ \  __ `/  __  /_  _ \_  ___/
                          \033[1;36m_  /  / / / /___  / /___      _  /___/ /_/ / /_/ // /_/ / /  __/  /    
                          \033[1;36m/_/  /_/  \____/  \____/      /_____/\____/\__,_/ \__,_/  \___//_/                                                                            

                                                         \033[1;31m[\033[1;39mC\033[1;31m]
\033[1;39m                                                    \033[1;35m For credits.
   \033[0;31m                                            Choose your favourite game.


                                      \033[1;31m[\033[1;39m1\033[1;31m] \033[1;32mMinecraft              \033[1;31m[\033[1;39m2\033[1;31m] \033[1;32mScreen Share
"""

while True:
    os.system('cls')
    print(nig)
    gg = Write.Input("             [×] >>  ", Colors.red_to_purple, interval=0.0025)
    if gg == '1':
        os.system('cls')
        print("                                             \033[1;39mLoading Minecraft Clients..")
        try:
            from consmath.minecraftt import openclient
            openclient()
        except Exception as e:
            print(f"Failed to open clients browser: {e}")
            input("Press ENTER to return...")
    elif gg == '2':
        os.system('cls')
        print("                                            \033[1;39mLoading Screen Share Tools Section..")
        try:
            from consmath.sstul import open_sstul
            open_sstul()
        except Exception as e:
            print(f"Failed to open SS-Tools menu: {e}")
            input("Press ENTER to return...")
    elif gg == 'C':
        os.system('cls')
        print("                                                   \033[1;39mLoading credits..")
        try:
            from consmath.credits import creditlisting, waitforit
            creditlisting()
            waitforit()
        except Exception as e:
            print(f"Failed to open credit list: {e}")
            input("Press ENTER to return...")