#!/usr/bin/python3
"""
Module contains netry point of the command interpreter
"""

import cmd
import json
import re
import sys
from models.base_model import BaseModel
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
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            obj = storage.classes()[line]()
            obj.save()
            print(obj.id)

    def help_show(self):
        start = "Prints the string represenation of an instance"
        end = " based on class name"
        print(f"{start}{end}")
        print()

    def do_show(self, line):
        line = line.split()
        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in storage.classes():
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
        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in storage.classes():
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
        if line and line not in storage.classes():
            print("** class doesn't exist **")
        elif line in storage.classes():
            objs = storage.all()
            lst = [str(obj) for id, obj in objs.items()
                   if type(obj).__name__ == line]
            print(lst)
        elif not line:
            lst = []
            objs = storage.all()
            for key in objs.keys():
                obj = str(objs[key])
                lst.append(obj)
            print(lst)

    def help_update(self):
        start = "Updates an instance based on class name"
        end = " and id by updating attribute"
        print(f"{start} {end}")
        beg = "Usage: update <class name> <id> <attribute name> "
        en = 'attribute value<>'
        print(f"{beg}{en}")
        print()

    def do_update(self, line):
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
                if re.search(r'\D', val) is not None:
                    val = str(val)
                else:
                    val_t = re.search(r'^\d{1,}["."]?\d*$', val)
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

    def default(self, line):
        """Catch input if it does not match specific processor command"""
        command_1 = re.search(r'^\w+\.\w+\(\)$', line)
        command_2 = re.search(r'^\w+\.\w+\(\".*\"\)$', line)
        if command_1 is not None and command_2 is None:
            com = command_1.group().split(".")
            c_name = com[0]
            method = com[1][:-2]
            methods = ["all", "count"]
            if c_name not in storage.classes():
                print(f"** class doesn't exist **")
            elif method not in methods:
                print(f"** action doesn't exist **")
            else:
                objs = storage.all()
                list_instances = [obj for id, obj in objs.items()
                                  if obj.to_dict()["__class__"] == c_name]
                if method == "all":
                    self.do_all(c_name)
                elif method == "count":
                    print(len(list_instances))
        elif command_2 is not None:
            com = command_2.group().split(".")
            c_name = com[0]
            method = com[1].split("(")[0]
            methods = ["update", "show", "destroy"]
            instance_id = com[1].split("(")
            instance_id = instance_id[1][:-1]
            if c_name not in storage.classes():
                print(f"** class doesn't exist **")
            elif method not in methods:
                print(f"** action doesn't exist **")
            else:
                objs = storage.all()
                key = c_name + "." + instance_id[1:-1]
                if instance_id == "":
                    print("** instance id missing **")
                elif key not in objs:
                    print("** no instance found **")
                else:
                    if method == "destroy":
                        del objs[key]
                        storage.save()
                    elif method =="show":
                        print(objs[key])
        else:
            print(f"*** Uknown syntax: {line}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        readline.parse_and_bind("tab: complete")
        HBNBCommand().onecmd(' '.join(sys.argv[1:]))
    else:
        HBNBCommand().cmdloop()
