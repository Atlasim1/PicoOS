import machine
print("Do you want to restart into NativeShell")
restartnative = input("y / n > ")
if restartnative == "y":
    print("Setting AUTOCHK_PATH Registry Key")
    key = open("/picoos/config/SYSTEM/boot/AUTOCHK_PATH", "w")
    key.write("/picoos/Programs/NativeShell/native.py")
    key.close()
    print("Scheduling Autochk")
    key = open("/picoos/config/SYSTEM/boot/AUTOCHK_SCHD", "w")
    key.write("True")
    key.close()
    print("Rebooting...")
    machine.soft_reset()
    