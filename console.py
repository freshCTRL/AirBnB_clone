#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.__init__ import storage


"""
This program is entry point for the airpnp
create your data model manage (create, update, destroy, etc) objects
via a console / command interpreter
store and persist objects to a file (JSON file)
"""


class HBNBCommand(cmd.Cmd):
    """The command interpter"""
    prompt = "(hbnb)"
    classes = ["BaseModel"]

    def do_create(self, *args):
        """
        Creates new instance of and prints its id and saves to  the storage
        """
        if len(args) == 0:
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
        obj_dic = storage.all()
        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args_list) == 1:
            print("** instance id missing **")
        else:
            print(obj_dic["{}.{}".format(args_list[0], args_list[1])])


    def do_EOF(self, arg):
        """Exits when CRTL+D is done"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
