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

    def do_EOF(self, line):
        """quits the intepreter"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return self.do_EOF

if __name__ == '__main__':
    HBNBCommand().cmdloop()
