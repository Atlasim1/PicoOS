import sys
import os
import gc
os.chdir("/") 
import cmd
print("Loaded Modules")


if "ENV_SYS_PROGRAM" in globals():
    print("*** Cannot Execute NATIVE Mode Program While In PROGRAM Mode ***")
    sys.exit(1)
else:
    print("")

if open("/picoos/config/SYSTEM/boot/AUTOCHK_SCHD.cfg").read() == "True":
    print("Preparing Disk Repair")
    exec(open("/picoos/config/SYSTEM/boot/AUTOCHK_PATH.cfg").read())


exec(open(open("/picoos/config/SYSTEM/boot/SERVICE_MANAGER_PATH.cfg").read()).read())
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
        try:
            exec(open(f"/picoos/boot/{CustomOsName}.py").read())
        except OSError:
            print("Not a valid operating system")
            
    elif selBootAction == "3":
        dir = os.listdir("/picoos/boot")
        print("\nList Of All Bootfiles\n-------------------------")
        print(*dir,sep = " | ")
        print("")
        
    elif selBootAction == "4":
        print("Booting More Options")
        moreOptionsOs = open("/picoos/config/SYSTEM/boot/DEFAULT_RECOVERY_PATH.cfg").read()
        exec(open(moreOptionsOs).read())
