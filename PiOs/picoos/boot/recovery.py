import sys
print("Welcome To Recovery Mode")
print("Please Choose Action :\n 1 : Reboot\n 2 : Boot Main BIOS\n 3 : Exit To REPL\n 4 : Launch Configuration Editor \n 5 : Launch SystemTools Runner\n 6 : Run Program")

while True:
    SelectedAction = input("Recovery > ")

    if SelectedAction == "1":
    #   import machine
        print("Rebooting ...")
    #   machine.soft_reset()
        
    elif SelectedAction == "2":
        print ("Entering BIOS")
        exec(open("/boot.py").read())
        
    elif SelectedAction == "3":
        sys.exit()
        
    elif SelectedAction == "4":
        exec(open("/picoos/systools/confedit.py").read())
        
    elif SelectedAction == "5":
        exec(open("/picoos/boot/SystoolRun.py").read())
        
    elif SelectedAction == "6":
        exec(open(input("Run Program > ")).read())
        
    else :
        print("Invalid Choice")
        

