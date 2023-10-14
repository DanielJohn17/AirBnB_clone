#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd
import json
from models import storage
from models.base_model import BaseModel
import re
import datetime


class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter."""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Handles End Of File character."""
        print()
        return True

    def do_quit(self, line):
        """Exits the program."""
        return True

    def emptyline(self):
        """Doesn't do anything on ENTER."""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        if not line:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            new_instance = storage.classes()[line]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance."""
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, line):
        """Prints all string representations of instances"""
        class_name = line.split()[0] if line else None

        if class_name:
            if class_name not in storage.classes():
                print("** class doesn't exist **")
            else:
                instances = []
                for key, obj in storage.all().items():
                    if type(obj).__name__ == class_name:
                        str_representation = str(obj)
                        instances.append(str_representation)
                print(instances)
        else:
            instances = [str(obj) for obj in storage.all().values()]
            print(instances)

    def do_update(self, line):
        """Updates an instance's attribute."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                attribute_name = args[2]
                attribute_value = args[3]
                obj = storage.all()[key]
                setattr(obj, attribute_name, attribute_value)
                obj.updated_at = datetime.datetime.now()
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
