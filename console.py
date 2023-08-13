#!/usr/bin/python3
"""
This program is entry point for the airpnp
create your data model manage (create, update, destroy, etc) objects
via a console / command interpreter
store and persist objects to a file (JSON file)
"""


import cmd
from models.__init__ import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    The command interpter
    """
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel}

    def do_create(self, *args):
        """
        Creates new instance of and prints its id and saves to  the storage
        """
        if len(*args) == 0:
            print("** class name missing **")
        else:
            try:
                new_obj = eval(args[0])()
                print(new_obj.id)
                storage.save()
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, args):
        """"
        Prints the string representation of an
        instance based on the class name and id
        """
        args_list = args.split()
        storage.reload()
        obj_dic = storage.all()
        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args_list) == 1:
            print("** instance id missing **")
        else:
            try:
                print(obj_dic["{}.{}".format(args_list[0], args_list[1])])
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        """
        import os
        import json
        args_list = args.split()
        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args_list) == 1:
            print("** instance id missing **")
        else:
            filename = f"file.json"
            if os.path.isfile(filename):
                with open(filename, mode="r", encoding="utf-8") as file:
                    b = json.loads(file.read())
                try:
                    del b["{}.{}".format(args_list[0], args_list[1])]
                    with open(filename, mode="w", encoding="utf-8") as file:
                        file.write(json.dumps(b))
                        file.close()
                    storage.reload()
                except KeyError:
                    print("** no instance found **")
            else:
                print("** no instance found **")

    def do_all(self, args):
        """
        prints the string repersention of all instances
        """
        storage.reload()
        args_list = args.split()
        objs_dic = storage.all()
        objs_list = [str(obj) for obj in objs_dic.values()]
        final_list = []
        if len(args_list) != 0:
            for ele in objs_list:
                if ele[:len(args_list[0]) + 2] == "[{}]".format(args_list[0]):
                    final_list.append(str(ele))
            print(final_list)
        else:
            print(objs_list)

    def do_update(self, args):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        """
        args_list = args.split()
        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args_list) == 1:
            print("** instance id missing **")
        elif len(args_list) == 2:
            print("** attribute name missing **")
        elif len(args_list) == 3:
            print("** value missing **")
        else:
            filename = f"file.json"
            if os.path.isfile(filename):
                with open(filename, mode="r", encoding="utf-8") as file:
                    b = json.loads(file.read())
                try:
                    b["{}.{}".format(args_list[0], args_list[1])]["{}".format(args_list[2)]] = args_list[3]
                    with open(filename, mode="w", encoding="utf-8") as file:
                        file.write(json.dumps(b))
                        file.close()
                    storage.reload()
                except KeyError:
                    print("** no instance found **")
            else:
                print("** no instance found **")

    def do_EOF(self, arg):
        """Exits when CRTL+D is done"""
        return True

    def emptyline(self):
        """does nothing when empty line is passed"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
