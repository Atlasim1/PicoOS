#Thread And Services Manager
def servicemessage(message):
    print("A Service on this device is reporting an error")
    servicemessage_wouldlike = input("Would you like to see this error?\n SERVICES (y / n) >>> ")
    if servicemessage_wouldlike == "y" or servicemessage_wouldlike == "yes":
        print(f"SERVICES : {message}")
        print("Message Receiving Done, You may now use your computer")
    else:
        print("Message Receiving Canceled, You may now use your computer")
    
servicelistraw = open("/picoos/config/SYSTEM/services/BOOT_SERVICES.cfg","r").read()
servicelist = []
servicelist = servicelistraw.split("\n")
runlistfile = "/picoos/service/runlist"

import _thread

def thread2():
    for service in servicelist:
        try:
            exec(open(f"/picoos/service/Services/{service}").read())
        except Exception as Error:
            servicemessage(f"ERROR : {Error}")
_thread.start_new_thread(thread2, ())
print("Started Services")