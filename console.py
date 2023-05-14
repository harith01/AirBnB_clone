#!/usr/bin/python3
"""Creates a Console"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Defines the console class"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Empty line command to not execute anything"""
        pass

    def do_create(self, arg):
        "Creates a new instance of arg"
        if not arg:
            print("** class name missing **")
            return
        if arg != "BaseModel":
            print("** class doesn't exist **")
            return
        obj = BaseModel()
        obj.save()
        print(obj.id)

    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id"""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id is missing **")
            return
        all_obj = storage.all()
        key_str = "{}.{}".format(args[0], args[1])
        if all_obj.get(key_str) is not None:
            print(all_obj[key_str])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if args[0] != 'BaseModel':
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id is missing **")
            return
        all_obj = storage.all()
        key_str = "{}.{}".format(args[0], args[1])
        if all_obj.get(key_str) is not None:
            del all_obj[key_str]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints string representation of all classes based or not
        on the class name"""
        if not arg and arg == "BaseModel":
            all_obj = storage.all()
            all_obj_list = []
            for key, obj in all_obj.items():
                all_obj_list.append(str(all_obj[key]))
            print(all_obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        the_dict = storage.all()
        key = "{}.{}".format(args[0], args[1])
        obj = the_dict.get(key)
        if obj == None:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(obj, args[2], args[3])

if __name__ == "__main__":
    HBNBCommand().cmdloop()
