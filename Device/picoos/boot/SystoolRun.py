import os, sys, machine

if "ENV_SYS_PROGRAM" in globals():
    print("*** Cannot Execute NATIVE Mode Program While In PROGRAM Mode ***")
    sys.exit(1)
else:
    print("")

runfile = None

global ENV_SYS_PROGRAM
ENV_SYS_PROGRAM = True

print("Welcome to PiOS SystemTools Runner")
print("Type \"list\" to list all SystemTools")
print("Type \"quit\" To Quit Program And Restart Computer")

os.chdir("/picoos/systools")

while True:
    runfile = input("Run System Tool > ")
    if runfile == "list":
        print("Listing All SystemTools")
        
        newsystooldir = []
        systooldir = os.listdir()
        for file in systooldir:
            newsystooldir.append(file.replace(".py",""))  
        print(*newsystooldir, sep = " \n ")
        
    elif runfile == "quit":
        machine.soft_reset()
            
    else:
        print(f"Running {runfile}")
        exec(open(runfile).read())
    

