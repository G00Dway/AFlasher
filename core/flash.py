import os
import time
import colorama
import sys
import scapy
from sys import platform
from colorama import Fore, Back, Style
colorama.init()
def image():
    img = input(Fore.CYAN+'[?]'+Fore.RESET+' Enter File Name Here (Without .img): ').strip(" ")
    print(Fore.YELLOW+'[+]'+Fore.RESET+' File: "'+img+'.img"')
    go = input(Fore.CYAN+'[?]'+Fore.RESET+' Is Your File Correct? (Y/n): ').strip(" ")
    if go == 'y' or go == 'Y' or go == 'yes' or go == 'YES':
        print(Fore.BLUE+'[*]'+Fore.RESET+' Rebooting To BootLoader...')
        os.system('adb reboot-bootloader > /dev/null 2>&1')
        print(Fore.BLUE+'[*]'+Fore.RESET+' Waiting 20 Seconds, For Device To Reboot...')
        time.sleep(20)
        print(Fore.BLUE+'[*]'+Fore.RESET+' Please Wait, Flashing IMG: "'+img+'.img"...')
        time.sleep(2)
        try:
            os.system('fastboot flash recovery '+img+'.img > /dev/null 2>&1')
        except:
            print(Fore.RED+'[-]'+Fore.RESET+' Error, Cannot Flash File '+img)
            print(Fore.BLUE+'[*]'+Fore.RESET+' Rebooting Device...')
            os.system('fastboot reboot > /dev/null 2>&1')
            exit()
        print(Fore.YELLOW+'[+]'+Fore.RESET+' Flash Success!')
        print(Fore.BLUE+'[*]'+Fore.RESET+' Rebooting Device...')
        os.system('fastboot reboot > /dev/null 2>&1')
        print(Fore.YELLOW+'[+]'+Fore.RESET+' File '+img+' Flashed Succesfully!')
        exit()
    elif go == 'n' or go == 'N' or go == 'no' or go == 'NO':
        image()
print(Fore.BLUE+'[*]'+Fore.RESET+' Please Move Your File To AFLASHERs Path! And Make Sure It Is (.img) File!')
time.sleep(0.5)
image()
