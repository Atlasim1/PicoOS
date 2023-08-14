import sys, os 
print("Disk Repair Initiated")
file = open("/picoos/config/SYSTEM/boot/AUTOCHK_SCHD.cfg", "w")
file.write("False")
file.close()
print("Disk Repair Finished")
