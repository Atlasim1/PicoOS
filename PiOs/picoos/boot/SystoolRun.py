import os, sys
print("Welcome to PiOS SystemTools Runner")
print("Type \"list\" to list all SystemTools")
print("Type \"recovery\" to open Recovery BootMenu")
print("Type\"quit\"To Quit Program")

os.chdir("/picoos/systools")

while True:
    runfile = "Run System Tool > "
    if runfile == "list":
        print("Listing All SystemTools")
        
        newsystooldir = []
        systooldir = os.listdir()
        for file in systooldir:
            newsystooldir.append(file.replace(".py",""))  
        print(*newsystooldir, sep = " \n ")
        
    elif runfile == "recovery":
        print("Booting Recovery Menu")
        moreOptionsOs = open("/picoos/config/SYSTEM/boot/DEFAULT_RECOVERY_PATH.cfg").read()
        exec(open(moreOptionsOs).read())
        
    elif runfile == "quit":
        sys.exit()
            
    else:
        break
    
print(f"Running {runfile}")
exec(open(runfile).read())
