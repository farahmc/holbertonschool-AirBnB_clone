#!/usr/bin/python3
"""
The entry point for the command intepreter
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    an interpreter class inheriting from cmd
    """
    prompt = '(hbnb) '

    def do_test(self, line):
        print("testing testing")

    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        return self.do_EOF

    def help_quit(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
