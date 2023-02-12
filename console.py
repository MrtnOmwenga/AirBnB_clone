#!/usr/bin/python3
"""
Module contains netry point of the command interpreter
"""

import cmd
import json
import re
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
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
    def help_create(self):
        print("Creates a new instance of BaseModel and saves it")
        print()

    def do_create(self, line):
        if not line:
            print("** class name missing **")
        elif line not in FileStorage.classes(self):
            print("** class doesn't exist **")
        else:
            obj = FileStorage.classes(self)[line]()
            obj.save()
            print(obj.id)

    def help_show(self):
        print("Prints the string represenation of an instance \ based on class name")
        print()

    def do_show(self, line):
        line = line.split()
        if len(line) == 0 :
            print("** class name missing **")
        elif line[0] not in FileStorage.classes(self):
            print("** class doesn't exist **")
        elif len(line) < 2:
            print("** instance id missing **")
        else:
            key = f"{line[0]}.{line[1]}"
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def help_destroy(self):
        print("Delets instance based on class name and id and save changes")
        print()

    def do_destroy(self, line):
        line = line.split()
        if len(line) == 0 :
            print("** class name missing **")
        elif line[0] not in FileStorage.classes(self):
            print("** class doesn't exist **")
        elif len(line) < 2:
            print("** instance id missing **")
        else:
            key = f"{line[0]}.{line[1]}"
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def help_all(self):
        print("Prints all string representation of all instances")
        print()

    def do_all(self, line):
        if line and line not in FileStorage.classes(self):
            print("** class doesn't exist **")
        elif line in FileStorage.classes(self):
            objs = storage.all()
            l = [str(obj) for id, obj in objs.items()
                 if type(obj).__name__ == line]
            print(l)
        elif not line:
            l = []
            objs = storage.all()
            for key in objs.keys():
                obj = str(objs[key])
                l.append(obj)
            print(l)

    def help_update(self):
        print("Updates an instance based on class name and id by updating attribute")
        print("Usage: update <class name> <id> <attribute name> 'attribute value<>")
        print()

    def do_update(self, line):
        l = line
        line = line.split()
        if not line:
            print("** class name missing **")
        elif line[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(line) == 1:
            print("** instance id missing **")
        else:
            key = f"{line[0]}.{line[1]}"
            if key not in storage.all():
                print("** no instance found **")
            elif len(line) < 3:
                print("** attribute name missing **")
            elif len(line) < 4:
                print("** value missing **")
            else:
                objs = storage.all()
                for obj_id in objs.keys():
                    obj = objs[obj_id]
                attr = str(line[2])
                val = line[3].replace('"', '')
                low = [chr(c) for c in range(97, 123)]
                up = [chr(c) for c in range(65, 91)]
                if val[0] in low or val[0] in up:
                    val = str(val)
                else:
                    val_t = re.search(r'^\d{1,}["."]?\d{1,}$', val)
                    if val_t.group():
                        if "." in val_t.group():
                            val = float(val)
                        else:
                            val = int(val)

                new_l = [c for c in attr]
                if "{" in new_l or "[" in new_l:
                    print("** attribute name missing **")
                else:
                    for key in obj.to_dict():
                        if attr is key:
                            obj[attr] = val
                        else:
                            setattr(obj, attr, val)
                        storage.save()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        readline.parse_and_bind("tab: complete")
        print(f"tt: {sys.argv[2]}")
        HBNBCommand().onecmd(' '.join(sys.argv[1:]))
    else:
        HBNBCommand().cmdloop()
