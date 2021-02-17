#!/usr/bin/python3
"""Defines console."""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Console class"""
    prompt = "(hbnb) "
    classe_list = {
        "BaseModel",
    }

    def emptyline(self):
        """
        Emptyline method to do nothing when press enter
        """
        pass

    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        """Quit command"""
        return True

    def do_destroy(self, line):
        """
        Deletes
        """
        itemA = line.split()
        old_storage = storage.all()
        if line == "":
            print("** class name missing **")
        elif line not in self.classe_list:
            print("** class doesn't exist **")
        elif len(line) < 2:
            print("** instance id missing **")
        elif (itemA[0] + "." + itemA[1]) not in storage.all():
            print("** no instance found **")
        else:
            key = itemA[0] + "." + itemA[1]
            if key in old_storage:
                del old_storage[key]
                storage.save()

    def do_show(self, line):
        """
        Prints the string representation
        """
        itemA = line.split()
        old_storage = storage.all()
        if line == "" or itemA == []:
            print("** class name missing **")
        elif len(line) < 2:
            print("** instance id missing **")
        elif line not in self.classe_list:
            print("** class doesn't exist **")
        elif (itemA[0] + "." + itemA[1]) not in storage.all():
            print("** no instance found **")
        else:
            key = itemA[0] + "." + itemA[1]
            if key in old_storage:
                print(old_storage[key])

    def do_create(self, line):
        """create <class> to create an object
        """
        if len(line) == 0:
            print("** class name missing **")
        elif line not in self.classe_list:
            print("** class doesn't exist **")
        else:
            if line == "BaseModel":
                obj = BaseModel()
                obj.save()
                print(obj.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
