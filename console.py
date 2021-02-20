#!/usr/bin/python3
"""Defines console."""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json
import ast


class HBNBCommand(cmd.Cmd):
    """Console class"""
    prompt = "(hbnb) "
    class_list = {
        "BaseModel",
        "User",
        "Place",
        "State",
        "City",
        "Amenity",
        "Review"
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
            setattr(StorageAll[key], item_arg[2], item_arg[3])
            storage.save()

    def do_count(self, className):
        """count the number of instances"""
        count = 0
        StorageAll = storage.all()
        for k in StorageAll:
            className_Stored = k.split(".")
            if className_Stored[0] == className:
                count += 1
        print(count)

    def default(self, arg):
        """default execution"""
        item_arg = arg.split(".")
        function_name = ""
        args = arg.split('.')
        objectName = item_arg[0]
        if len(item_arg) >= 2:
            function_name = item_arg[1]
            uid_value = item_arg[1].split("\"")
            arg_com = function_name.split(',')
            arg_comB = function_name.split(', {')
            if function_name == "all()":
                self.do_all(objectName)
            elif function_name == "count()":
                self.do_count(objectName)
            elif function_name == "show(\"" + uid_value[1] + "\")":
                self.do_show(objectName + " " + uid_value[1])
            elif function_name == "destroy(\"" + uid_value[1] + "\")":
                self.do_destroy(objectName + " " + uid_value[1])
            if len(arg_comB) == 2:
                arg_comB[1] = arg_comB[1][0:len(arg_comB[1]) - 1]
                tmp1 = "{" + arg_comB[1]
                syntax = "update(\"{}\", {})"
                if function_name == syntax.format(uid_value[1], tmp1):
                    tmp = tmp1.replace("'", "\"")
                    d = json.loads(tmp)
                    syntax = "{} {} {} {}"
                    for k in d:
                        self.do_update(syntax.format(objectName,
                                                     uid_value[1],
                                                     k,
                                                     d[k]))
            elif len(arg_com) == 3:
                arg_com[1] = arg_com[1][2: len(arg_com[1]) - 1]
                arg_com[2] = arg_com[2][2: len(arg_com[2]) - 2]
                syntax = "update(\"{}\", \"{}\", \"{}\")"
                if function_name == syntax.format(uid_value[1],
                                                  arg_com[1],
                                                  arg_com[2]):
                    syntax = "{} {} {} {}"
                    self.do_update(syntax.format(objectName,
                                                 uid_value[1],
                                                 arg_com[1],
                                                 arg_com[2]))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
