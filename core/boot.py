import os
import sys
import colorama
import time
import scapy
from sys import platform
from colorama import Fore, Back, Style
colorama.init()
print(Fore.BLUE+'[*]'+Fore.RESET+' Please Make Sure You Have Turned On "OEM Unlocking"!')
time.sleep(2)
print(Fore.BLUE+'[*]'+Fore.RESET+' Rebooting Device To BootLoader...')
try:
    os.system('adb reboot-bootloader > /dev/null 2>&1')
except:
    print(Fore.RED+'[-]'+Fore.RESET+' Error Has Been Ocurred! Cannot Reboot To BootLoader...')
    exit()
print(Fore.BLUE+'[*]'+Fore.RESET+' Waiting 20 Seconds To Complete Reboot...')
time.sleep(20)
print(Fore.BLUE+'[*]'+Fore.RESET+' Unlocking BootLoader...')
time.sleep(3)
try:
    os.system('fastboot oem unlock > /dev/null 2>&1')
except:
    print(Fore.RED+'[-]'+Fore.RESET+' Error Has Been Ocurred! Cannot Unlock BootLoader...')
    exit()
print(Fore.YELLOW+'[+]'+Fore.RESET+' BootLoader Unlocked Succesfully!')
print(Fore.BLUE+'[*]'+Fore.RESET+' Rebooting Device...')
os.system('fastboot reboot > /dev/null 2>&1')
print(Fore.YELLOW+'[+]'+Fore.RESET+' Device BootLoader Unlocking Completed!')
exit()