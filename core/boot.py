import os
import sys
import colorama
import time
import scapy
from sys import platform
from colorama import Fore, Back, Style
colorama.init()
print(Fore.BLUE+'[*]'+Fore.WHITE+' Please Make Sure You Have Turned On "OEM Unlocking"!')
time.sleep(2)
print(Fore.BLUE+'[*]'+Fore.WHITE+' Rebooting Device To BootLoader...')
try:
    os.system('adb reboot-bootloader > /dev/null 2>&1')
except:
    print(Fore.RED+'[-]'+Fore.WHITE+' Error Has Been Ocurred! Cannot Reboot To BootLoader...')
    exit()
print(Fore.BLUE+'[*]'+Fore.WHITE+' Waiting 20 Seconds To Complete Reboot...')
time.sleep(20)
print(Fore.BLUE+'[*]'+Fore.WHITE+' Unlocking BootLoader...')
time.sleep(3)
try:
    os.system('fastboot oem unlock > /dev/null 2>&1')
except:
    print(Fore.RED+'[-]'+Fore.WHITE+' Error Has Been Ocurred! Cannot Unlock BootLoader...')
    exit()
print(Fore.YELLOW+'[+]'+Fore.WHITE+' BootLoader Unlocked Succesfully!')
print(Fore.BLUE+'[*]'+Fore.WHITE+' Rebooting Device...')
os.system('fastboot reboot > /dev/null 2>&1')
print(Fore.YELLOW+'[+]'+Fore.WHITE+' Device BootLoader Unlocking Completed!')
exit()
