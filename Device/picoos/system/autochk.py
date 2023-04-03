import sys, os 

if "ENV_SYS_PROGRAM" in globals():
    print("*** Cannot Execute NATIVE Mode Program While In PROGRAM Mode ***")
    sys.exit(1)
else:
    print("Disk Repair Initiated")
    file = open("/picoos/config/SYSTEM/boot/AUTOCHK_SCHD.cfg", "w")
    file.write("False")
    file.close()
    print("Disk Repair Finished")