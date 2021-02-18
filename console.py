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
        "User"
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

    def do_update(self, arg):
        """
        Update an instance base on class name id
        Usage: update <class name> <id> <attribute name> "<attribute value>"
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
        elif len(item_arg) < 3:
            print("** attribute name missing **")
        elif len(item_arg) < 4:
            print("** value missing **")
        else:
            key = item_arg[0] + "." + item_arg[1]
            print(StorageAll[key])
            print(type(StorageAll[key]))
            setattr(StorageAll[key], item_arg[2], item_arg[3])
            storage.save()
if __name__ == '__main__':
    HBNBCommand().cmdloop()
