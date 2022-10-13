import sys
print("Welcome To Recovery Mode")
print("Please Choose Action :\n 1 : Reboot\n 2 : Boot Main BIOS\n 3 : Exit To REPL")

while True
    SelectedAction = input("Recovery > ")

    if SelectedAction == "1":
        import machine
        print("Rebooting ...")
        machine.soft_reset()
        
    elif SelectedAction == "2":
        print ("Entering BIOS")
        exec(open("/boot.py").read())
        
    elif SelectedAction == "3":
        sys.exit()
        
    else :
        print("Invalid Choice")
        

