#Thread And Services Manager

servicelistraw = open("/picoos/config/SYSTEM/services/BOOT_SERVICES.cfg","r").read()
servicelist = []
servicelist = servicelistraw.split("\n")
runlistfile = "/picoos/service/runlist"

import _thread

def thread2():
    for service in servicelist:
        exec(open(f"/picoos/service/Services/{service}").read())
                        
_thread.start_new_thread(thread2, ())
print("Started Services")