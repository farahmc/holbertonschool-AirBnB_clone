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
    classes_list = ["BaseModel", "User", "State", "City",
                  "Amenity", "Place", "Review"]

    def do_EOF(self, line):
        """quits the intepreter"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return self.do_EOF

    def do_create(self, line):
        """
        Creates a new instance of specified class and prints
        object's unique id
        """
        if not line:
            print("** class name missing **")
            return

        args = line.split()

        if args[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
            return

        cls_name = globals()[args[0]]
        new_obj = cls_name()
        print(new_obj.id)

    def show(self, line):
        """
        prints the string repr of an instance based
        on class name and id
        """
        if not line:
            print("** class name missing **")
            return

        args = line.split()

        if args[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")

        if len(args) < 2:
            print("** instance id missing **")

        cls_name = globals()[args[0]]
        id_check = int(args[1])

        print(cls_name)
        print(id_check)

    def destroy(self, line):
        pass

    def all(self, line):
        pass

    def update(self, line):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop(intro="Python stinks")
