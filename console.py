#!/usr/bin/python3
"""
The entry point for the command intepreter
"""

import cmd.Cmd

class HBNBCommand(cmd.Cmd):
    """
    an interpreter class inheriting from Cmd
    """
    def __init__(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
