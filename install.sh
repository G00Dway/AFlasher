sleep 1
clear
echo -e "\033[1;34m[*] \033[0mInstalling Requirements...."
apt install adb fastboot python -y > /dev/null 2>&1
pip3 install colorama pgrep scapy > /dev/null 2>&1
pip2 install pgrep colorama scapy > /dev/null 2>&1
echo -e "\033[1;34m[*] \033[0mCleaning Up..."
apt clean > /dev/null 2>&1
echo -e "\033[1;32m[+] \033[0mInstallation Finished!"
#\033[1;77m[i] \033[0m
#\033[1;77m[?] \033[0m
#\033[1;32m[+] \033[0m
#\033[1;33m[!] \033[0m
#\033[1;31m[-] \033[0m
#\033[1;34m[*] \033[0m