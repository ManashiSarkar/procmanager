#!/usr/bin/env python3

import os

class Command():
    def __init__(self, args):
        pass

class ListProcs(Command):
    def __init__(self, args):
        pass

    def run(self):
        proc = "/proc"
        for d in os.listdir("/proc"):
            if os.path.isdir(proc + "/" + d) and d.isdigit():
                print(d)

class CommandAndArgs(Command):
    def __init__(self, args):
        self.args = args

    def run(self):
        if len(self.args) != 1:
            print ("There should be exactly 1 argument, the PID")
            return
        pid = self.args[0]
        try:
            with open("/proc/"+str(pid)+"/cmdline") as arglist:
                args = arglist.read().split("% ")
                for arg in args:
                    print(arg)
        except:
            print ("PID does not correspond to a process at the moment")
            

commands = {
    "list" : lambda args: ListProcs(args),
    "caa" : lambda args: CommandAndArgs(args)
}

def get_command():
    strs = input(">").split(" ")
    #cmd = None
    try:
        return commands[strs[0]](strs[1:])
    except KeyError as e:
        print("Unknown command")
    #return cmd

while True:
    cmd = get_command()
    cmd.run()