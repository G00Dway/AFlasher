import colorama
import sys
import scapy
import os
import time
from sys import platform
from colorama import Fore, Back, Style
colorama.init()
if platform == 'win32' or platform =='win64':
    os.system('cls')
else:
    os.system('clear')
time.sleep(2)
def banner():
    print('''
  ___  ______ _           _               
 / _ \ |  ___| |         | |              
/ /_\ \| |_  | | __ _ ___| |__   ___ _ __ 
|  _  ||  _| | |/ _` / __| '_ \ / _ \ '__| ======
| | | || |   | | (_| \__ \ | | |  __/ |   ======
\_| |_/\_|   |_|\__,_|___/_| |_|\___|_|   =====
                              
Made By  :{ G00Dway }
Github   :{ https://github.com/G00Dway }

Android Flasher '''+Fore.YELLOW+'''V.0.8'''+Fore.RESET+'''
=====================''')
banner()
time.sleep(0.4)
def main():
    try:
        root = input(Fore.BLUE+'''
1) '''+Fore.RESET+'''Flash Files'''+Fore.BLUE+'''
2) '''+Fore.RESET+'''Unlock BootLoader'''+Fore.BLUE+'''
3) '''+Fore.RESET+'''Check For Updates'''+Fore.BLUE+'''
4) '''+Fore.RESET+'''Exit'''+Fore.RED+'''

>>> Android-Flasher$ '''+Fore.RESET).strip(" ")
    except KeyboardInterrupt:
        print('')
        print(Fore.RED+'[-]'+Fore.RESET+' Exiting...')
        exit()
    if root == '1':
        try:
            os.system('python3 core/flash.py')
        except:
            print(Fore.RED+'[-]'+Fore.RESET+' Error Has Been Ocurred! Cannot Run The File...')
            exit()
    elif root == '2':
        try:
            os.system('python3 core/boot.py')
        except:
            print(Fore.RED+'[-]'+Fore.RESET+' Error Has Been Ocurred! Cannot Run The File...')
            exit()
    elif root == '3':
        os.system('bash core/update_check.sh')
        time.sleep(1)
        print(Fore.YELLOW+'-------------------------'+Fore.RESET)
        main()
    elif root == '4':
        exit()
    else:
        print(Fore.RED+'[-]'+Fore.RESET+' Unrecognized Command: "'+root+'"')
        time.sleep(1)
        if platform == 'win32' or platform == 'win64':
            os.system('cls')
            banner()
            time.sleep(0.5)
            main()
        else:
            os.system('clear')
            banner()
            time.sleep(0.5)
            main()
main()
