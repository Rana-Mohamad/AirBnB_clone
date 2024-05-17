#!/usr/bin/python3
''' Console module. '''


import cmd


class HBNBCommand(cmd.Cmd):
    ''' HBNBCommand class. '''

    prompt = "(hbnb) "

    def do_quit(self, arg):
        '''Quit command to exit the program'''

        return True

    def help(self, arg):
        ''' help quit method. '''

        print("Quit command to exit the program")

    def do_EOF(self, arg):
        ''' EOF method. '''

        print()
        return True

    def emptyline(self):
        ''' Do nothing when an empty line entered. '''

        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
