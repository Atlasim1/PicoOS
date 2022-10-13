import sys
import os
import gc
os.chdir("/") 
import cmd
print("Loaded Modules")
booted = True
while booted == True:
    print("Please Choose Action : \n 1 : Boot Default OS\n 2 : Boot Custom OS\n 3 : List All Bootfiles\n 4 : More Options")
    selBootAction = input("Boot > ")

    if selBootAction == "1":
        print("Booting Default Operating System\n")
        defaultOs = open("/picoos/config/SYSTEM/boot/DEFAULT_BOOT_PATH.cfg").read()
        booted = False
        exec(open(defaultOs).read())
        
    elif selBootAction == "2":
        CustomOsName = input("Please Enter Operating System Name > ")
        print(f"Booting {CustomOsName}...\n")
        booted = False
        exec(open(f"/picoos/boot/{CustomOsName}.py").read())

    elif selBootAction == "3":
        dir = os.listdir("/picoos/boot")
        print("\nList Of All Bootfiles\n-------------------------")
        print(*dir,sep = " | ")
        print("")
        
    elif selBootAction == "4":
        print("Booting More Options")
        moreOptionsOs = open("/picoos/config/SYSTEM/boot/DEFAULT_RECOVERY_PATH.cfg").read()
        exec(open(moreOptionsOs).read())
