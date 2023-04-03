#PiOS Configuration editor
PROGRAM_VERSION = "1.0.0"
PROGRAM_BUILD = "Y23W03V1"

import os, cmd, sys

olddir = os.getcwd()

os.chdir("/picoos/config")

class configshell(cmd.Cmd):
    intro = "Welcome to the Configuration Editor\nType help to list all commands\n"
    prompt = f"{os.getcwd()} > ".replace("/picoos/config","CONFIG")
    
    def do_listkeys(self, args):
        keydir = []
        configdir = os.listdir()
        for config in configdir:
            if ".cfg" in config:
                keydir.append(config.replace(".cfg","")) 
        print(*keydir, sep = " \n ")
        
    def do_lsk(self, args):
        keydir = []
        configdir = os.listdir()
        for config in configdir:
            if ".cfg" in config:
                keydir.append(config.replace(".cfg","")) 
        print(*keydir, sep = "\n")
        
#    def do_listheaderkeys(self, args):
#        hkeydir = []
#        alldir = os.listdir()
#        for hkey in alldir:
#            if ".cfg" in hkey:
#                print()
#            else:
#                alldir.append(hkey)    
#        print(*hkeydir, sep = "\n")

#    def do_lshk(self, args):
#        hkeydir = []
#        alldir = os.listdir()
#        for hkey in alldir:
#            if ".cfg" in hkey:
#                print()
#            else:
#                alldir.append(hkey)    
#        print(*hkeydir, sep = "\n")
#
    def do_ls(self, args):
        alldir = os.listdir()
        print(*alldir, sep = "\n")
        
    def do_cd(self, args):
        os.chdir(args)
        print(f"Changed Path to {args}")
        
    def do_readkey(self, args):
        key = open(f"{args}.cfg","r").read()
        print(f"{args} << {key}")
        
    def do_writekey(self, args):
        file = open(args[0],"a")
        file.write(args[1])
        file.close
        
    def do_mkhkey(self, args):
        os.mkdir(args)
        
    def do_rmkey(self, args):
        os.remove(f"{args}.cfg")
        
    def do_rmhkey(self, args):
        os.rmdir(args)
        
    def do_quit(self, args):
        os.chdir(olddir)
        sys.exit()
        
    def do_version(self, args):
        print(f"PiOS Configuration Editor\nVersion {PROGRAM_VERSION} Build {PROGRAM_BUILD}")
        
    def do_help(self, args):
        print(f"""
              PiOS Configuration Editor 
              Version {PROGRAM_VERSION} Build {PROGRAM_BUILD}
              --------------------
              Help Documentation : 
              
               - listkeys : List all keys in current path AKA : lsk
              
               - listheaderkeys : List all header keys in current path AKA : lshk
              
               - ls : List all elements in current path
              
               - cd <path> : Change current path
              
               - readkey <key> : Prints contents of key
              
               - writekey <key> <data> : Modify contents of key or create new key
              
               - mkhkey <hkey> : Create new header key
              
               - rmkey <key> : Remove Key from config
              
               - rmhkey <hkey> : Remove Header key. Key must be empty
               
               - quit : Quit Program
               
              """)


if __name__ == "__main__":
    configshell().cmdloop()
    
