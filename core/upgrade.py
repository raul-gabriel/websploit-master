#!/usr/bin/env python3
#
# Websploit FrameWork Upgrade Module
# Created By 0x0ptim0us (Fardin Allahverdinazhand)
# Email : 0x0ptim0us@Gmail.Com

import os
import urllib.request
from time import sleep
from core import wcolors
import webbrowser

def upgrade():
    print(wcolors.color.BOLD + wcolors.color.BLUE + "[*]Checking For New Version, Please Wait ..." + wcolors.color.ENDC)
    try:
        with urllib.request.urlopen("http://sourceforge.net/projects/websploit/files/") as cu:
            res = cu.read().decode('utf-8')
            if 'WebSploit Framework V.3.0.1' in res:
                print(wcolors.color.GREEN + "[*]New Version Available")
                sleep(2)
                print("[*]Download Latest Version : https://sourceforge.net/projects/websploit/files/latest/download?source=files" + wcolors.color.ENDC)
                print(wcolors.color.CYAN + "[*]Starting Browser To Download Location, Please Wait ..." + wcolors.color.ENDC)
                sleep(2)
                webbrowser.open("https://sourceforge.net/projects/websploit/files/latest/download?source=files")
            else:
                print(wcolors.color.BOLD + wcolors.color.RED + "[*]New Version Not Available, This Is Latest Version Of The WebSploit Framework." + wcolors.color.ENDC)
                sleep(4)
    except urllib.error.URLError:
        print(wcolors.color.BOLD + wcolors.color.RED + "[*]Connection Timeout, Check Your Internet Connection!" + wcolors.color.ENDC)

if __name__ == "__main__":
    upgrade()
