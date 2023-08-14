import sys
import os
import gc
os.chdir("/") 
import cmd
print("Loaded Modules")

#Run Autochk if scheduled
if open("/picoos/config/SYSTEM/boot/AUTOCHK_SCHD.cfg").read() == "True":
    print("Preparing Disk Repair")
    exec(open("/picoos/config/SYSTEM/boot/AUTOCHK_PATH.cfg").read())

#Thread And Services Manager
def servicemessage(message): # service output function
    print("A Service on this device is reporting an error")
    servicemessage_wouldlike = input("Would you like to see this error?\n SERVICES (y / n) >>> ")
    if servicemessage_wouldlike == "y" or servicemessage_wouldlike == "yes":
        print(f"SERVICES : {message}")
        print("Message Receiving Done, You may now use your computer")
    else:
        print("Message Receiving Canceled, You may now use your computer")
        
#get list of services needed to boot
servicelistraw = open("/picoos/config/SYSTEM/services/BOOT_SERVICES.cfg","r").read()
servicelist = []
servicelist = servicelistraw.split("\n")

runlistfilepath = "/picoos/service/runlist" #why is this here?

import _thread
try:
    if open("/picoos/config/SYSTEM/services/NO_SERVICES_BOOT.cfg").read() == "False": 
        def thread2():
            for service in servicelist:
                try:
                    exec(open(f"/picoos/service/Services/{service}").read())
                except Exception as Error:
                    servicemessage(f"ERROR : {Error}")
        _thread.start_new_thread(thread2, ())
        print("Started Services")
    elif open("/picoos/config/SYSTEM/boot/NO_SERVICES_BOOT.cfg").read() == "True":
        print("Boot requested without services, Booting without services (System may be unstable")
except OSError:
    print("Missing File Error (Probably Missing Key?)")
#---

#Selector/Bootmenu
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
