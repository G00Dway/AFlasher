echo -e "\033[1;34m[*] \033[0mChecking For Updates..."
BRANCH="main"
LAST_UPDATE=`git show --no-notes --format=format:"%H" $BRANCH | head -n 1`
LAST_COMMIT=`git show --no-notes --format=format:"%H" origin/$BRANCH | head -n 1`

git remote update > /dev/null 2>&1
if [ $LAST_COMMIT != $LAST_UPDATE ]; then
        echo -e "\033[1;34m[*] \033[0mUpdating To Latest Version..."
        git pull --no-edit > /dev/null 2>&1
        echo -e "\033[1;32m[+] \033[0mUpdate Successfull!"
else
        echo -e "\033[1;32m[+] \033[0mNo updates Available!"
fi
#\033[1;77m[i] \033[0m
#\033[1;77m[?] \033[0m
#\033[1;32m[+] \033[0m
#\033[1;33m[!] \033[0m
#\033[1;31m[-] \033[0m
#\033[1;34m[*] \033[0m