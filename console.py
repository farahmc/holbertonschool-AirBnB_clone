#!/usr/bin/python3
"""
The entry point for the command intepreter
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
import copy


class HBNBCommand(cmd.Cmd):
    """
    an interpreter class inheriting from cmd
    """
    prompt = '(hbnb) '
    classes_list = ["BaseModel", "User", "State", "City",
                    "Amenity", "Place", "Review"]

    def do_EOF(self, line):
        """quits the intepreter"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return self.do_EOF

    def do_create(self, line):
        """
        Creates a new instance of specified class and prints
        instance's unique id
        """
        if not line:
            print("** class name missing **")
            return

        args = line.split()

        if args[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
            return

        new_obj = globals()[args[0]]()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, line):
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
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_key = args[0] + "." + args[1]
        storage = FileStorage()
        all_objs = storage.all()

        for key, value in all_objs.items():
            if key == obj_key:
                print(value)
                return
        print("** no instance found **")

    def do_destroy(self, line):
        """
        deletes an instance of a class based on class name and id
        save changes to json file
        """
        if not line:
            print("** class name missing **")
            return

        args = line.split()

        if args[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_key = args[0] + "." + args[1]
        storage = FileStorage()
        all_objs = storage.all()

        for key, value in all_objs.items():
            if key == obj_key:
                del all_objs[key]
                print(all_objs)
                storage.__objects = copy.deepcopy(all_objs)
                storage.save()
                return

        print("** no instance found **")

    def do_all(self, line):
        """
        prints, as a list of strings, the string repr of all instances
        or all instances of a certain class if provided
        """
        objs_list = []
        storage = FileStorage()
        all_objs = storage.all()

        if not line:
            for key, value in all_objs.items():
                objs_list.append(str(value))
            print(objs_list)
            return
        else:
            args = line.split()
            print("not sure yet")

    def update(self, line):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop(intro="Python stinks")
