#!/usr/bin/python3
"""Defines console."""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Console class"""
    prompt = "(hbnb) "
    classe_list = {
        "BaseModel",
    }

    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        """Quit command"""
        return True

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
