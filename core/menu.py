#!/usr/bin/env python3
#
# WebSploit FrameWork Menu module
# Created By 0x0ptim0us (Fardin Allahverdinazhand)
# Email : 0x0ptim0us@Gmail.Com

from core import wcolors

def main_info():
    ston = wcolors.color.BLUE + "[" + wcolors.color.ENDC
    print("")
    print("\t\t--=" + ston + wcolors.color.GREEN + "WebSploit Advanced MITM Framework" + wcolors.color.ENDC)
    print("\t\t--=" + ston + wcolors.color.GREEN + "Reescrito por Raúl Gabriel (Cusco - Perú)" + wcolors.color.ENDC)
    print("\t+---**---==" + ston + "Version :" + wcolors.color.RED + "3.0.0" + wcolors.color.ENDC)
    print("\t+---**---==" + ston + "Codename :" + wcolors.color.RED + "Katana" + wcolors.color.ENDC)
    print("\t+---**---==" + ston + "Available Modules : " + wcolors.color.GREEN + "20" + wcolors.color.ENDC)
    print("\t\t--=" + ston + "Fecha de actualizacion: [" + wcolors.color.RED + "r3.pyth0.0-000 20.9.2014" + wcolors.color.ENDC + "]")
    print("\n\n")

if __name__ == "__main__":
    main_info()
