#!/usr/bin/python3
"""
The entry point for the command intepreter
"""

import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    an interpreter class inheriting from cmd
    """
    prompt = '(hbnb) '
    class_list = ["BaseModel"]

    def do_EOF(self, line):
        """quits the intepreter"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return self.do_EOF

    def do_create(self, line):
        """creates a new instance"""
        if len(line) == 0:
            print("** class name missing **")
            return
        if line not in cls.class_list:
            print("** class doesn't exist **")
            return
        new_obj = line[0]()
        print(new_obj.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop(intro="Python stinks")
