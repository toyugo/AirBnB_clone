#!/usr/bin/python3
"""Defines console."""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Console class"""
    prompt = "(hbnb) "
    class_list = {
        "BaseModel",
    }

    def emptyline(self):
        """
        Emptyline method to do nothing when press enter
        """
        pass

    def do_EOF(self, arg):
        return True

    def do_quit(self, arg):
        """Quit command"""
        return True

    def do_destroy(self, arg):
        """
        Deletes
        """
        item_arg = arg.split()
        StorageAll = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif item_arg[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(item_arg) < 2:
            print("** instance id missing **")
        elif (item_arg[0] + "." + item_arg[1]) not in StorageAll:
            print("** no instance found **")
        else:
            key = item_arg[0] + "." + item_arg[1]
            if key in StorageAll:
                del StorageAll[key]
                storage.save()

    def do_show(self, arg):
        """Prints the string representation"""
        item_arg = arg.split()
        StorageAll = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif item_arg[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(item_arg) < 2:
            print("** instance id missing **")
        elif (item_arg[0] + "." + item_arg[1]) not in StorageAll:
            print("** no instance found **")
        else:
            key = item_arg[0] + "." + item_arg[1]
            if key in StorageAll:
                print(StorageAll[key])

    def do_create(self, arg):
        """create <class> to create an object"""
        item_arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif item_arg[0] not in self.class_list:
            print("** class doesn't exist **")
        else:
            for obj in self.class_list:
                if arg == obj:
                    newObj = eval(obj + "()")
                    newObj.save()
                    print(newObj.id)

    def do_all(self, arg):
        """Prints all string representation"""
        item_arg = arg.split()
        StorageAll = storage.all()
        listAll = []
        if len(arg) == 0:
            for k in StorageAll:
                listAll.append(str(StorageAll[k]))
            print(listAll)
        elif item_arg[0] not in self.class_list:
            print("** class doesn't exist **")
        else:
            for k in StorageAll:
                tmp = k.split(".")
                if tmp[0] == item_arg[0]:
                    listAll.append(str(StorageAll[k]))
            print(listAll)
if __name__ == '__main__':
    HBNBCommand().cmdloop()
