#!/usr/bin/python3
"""Creates a Console"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models import storage


classes = ['BaseModel',
           'User',
           'Place',
           'City',
           'Amenity',
           'State',
           'Review']


def line_parser(line):
    """Parses the parameters of console command
    into a dictionary"""
    kwargs = {}
    args = line.split(" ")
    class_name = args[0]
    params = args[1:]
    for param in params:
        if "=" in param:
            param = param.split("=")
            key = param[0]
            value = param[1]
            if value[0] == value[-1] == '"':
                value = value.strip('/"').replace("_", " ")
            else:
                try:
                    value = eval(value)
                except Exception:
                    continue
            if type(value) not in [int, str, float]:
                continue
            else:
                kwargs[key] = value
        else:
            continue
    return class_name, kwargs


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
        class_name, kwargs = line_parser(arg)
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        obj = eval(class_name)(**kwargs)
        obj.save()
        print(obj.id)

    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id"""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if args[0] not in classes:
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
        if args[0] not in classes:
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

    def do_all(self, args):
        """Prints string representation of all classes based or not
        on the class name"""
        if args != "":
            args = args.split()
            if args[0] in classes:
                all_obj = storage.all()
                all_obj_list = []
                for key, obj in all_obj.items():
                    all_obj_list.append(str(obj))
                print(all_obj_list)
            else:
                print("** class doesn't exist **")
        else:
            all_obj_list = [str(obj) for key, obj in storage.all().items()]
            print(all_obj_list)

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        the_dict = storage.all()
        key = "{}.{}".format(args[0], args[1])
        obj = the_dict.get(key)
        if obj is None:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(obj, args[2], args[3])
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
