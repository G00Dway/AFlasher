import os
import time
import colorama
import sys
import scapy
from sys import platform
from colorama import Fore, Back, Style
colorama.init()
def image():
    img = input(Fore.CYAN+'[?]'+Fore.WHITE+' Enter File Name Here (Without .img): ').strip(" ")
    print(Fore.YELLOW+'[+]'+Fore.WHITE+' File: "'+img+'.img"')
    go = input(Fore.CYAN+'[?]'+Fore.WHITE+' Is Your File Correct? (Y/n): ').strip(" ")
    if go == 'y' or go == 'Y' or go == 'yes' or go == 'YES':
        print(Fore.BLUE+'[*]'+Fore.WHITE+' Rebooting To BootLoader...')
        os.system('adb reboot-bootloader > /dev/null 2>&1')
        print(Fore.BLUE+'[*]'+Fore.WHITE+' Waiting 20 Seconds, For Device To Reboot...')
        time.sleep(20)
        print(Fore.BLUE+'[*]'+Fore.WHITE+' Please Wait, Flashing IMG: "'+img+'.img"...')
        time.sleep(2)
        try:
            os.system('fastboot flash recovery '+img+'.img > /dev/null 2>&1')
        except:
            print(Fore.RED+'[-]'+Fore.WHITE+' Error, Cannot Flash File '+img)
            print(Fore.BLUE+'[*]'+Fore.WHITE+' Rebooting Device...')
            os.system('fastboot reboot > /dev/null 2>&1')
            exit()
        print(Fore.YELLOW+'[+]'+Fore.WHITE+' Flash Success!')
        print(Fore.BLUE+'[*]'+Fore.WHITE+' Rebooting Device...')
        os.system('fastboot reboot > /dev/null 2>&1')
        print(Fore.YELLOW+'[+]'+Fore.WHITE+' File '+img+' Flashed Succesfully!')
        exit()
    elif go == 'n' or go == 'N' or go == 'no' or go == 'NO':
        image()
print(Fore.BLUE+'[*]'+Fore.WHITE+' Please Move The .img File To AFLASHERs Path!')
time.sleep(0.5)
image()
