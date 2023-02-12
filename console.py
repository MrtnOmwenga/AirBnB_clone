#!/usr/bin/python3
"""
Module contains netry point of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """This class provides entry point for the cmd interpreter"""
    prompt = ("(hbnb) ")

    def help_quit(self):
        print("Quit command to exit the program")
        print()

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        """EOF commad to exit the program"""
        return True

    def emptyline(self):
        """Disable repetition of last command entered"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
