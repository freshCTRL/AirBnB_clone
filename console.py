#!/usr/bin/python3
import cmd
"""
This program is entry point for the airpnp
create your data model manage (create, update, destroy, etc) objects
via a console / command interpreter
store and persist objects to a file (JSON file)
"""


class HBNBCommand(cmd.Cmd):
    """The command interpter"""
    prompt = "(hbnb)"

    def do_EOF(self, arg):
        """Exits when CRTL+D is done"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
