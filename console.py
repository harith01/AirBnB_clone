#!/usr/bin/python3
"""Creates a Console"""
import cmd

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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
