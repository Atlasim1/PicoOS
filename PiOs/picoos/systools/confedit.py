import os, cmd
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