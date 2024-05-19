#!/usr/bin/python3
''' Console module. '''


import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import re
import ast


class HBNBCommand(cmd.Cmd):
    ''' HBNBCommand class. '''

    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "Place", "State",
                     "City", "Amenity", "Review"]

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

    def do_create(self, arg):
        '''
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        '''

        commands = shlex.split(arg)

        if (len(commands) == 0):
            print("** class name missing **")

        elif (commands[0] not in self.valid_classes):
            print("** class doesn't exist **")

        else:
            new_inst = eval(f"{commands[0]}()")
            storage.save()
            print(new_inst.id)

    def do_show(self, arg):
        '''
        Prints the string representation of an
        instance based on the class name and id.
        '''

        commands = shlex.split(arg)

        if (len(commands) == 0):
            print("** class name missing **")

        elif (commands[0] not in self.valid_classes):
            print("** class doesn't exist **")

        elif (len(commands) < 2):
            print("** instance id missing **")

        else:
            objs = storage.all()

            key = "{}.{}".format(commands[0], commands[1])

            if (key in objs):
                print(objs[key])

            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        '''
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        '''

        commands = shlex.split(arg)

        if (len(commands) == 0):
            print("** class name missing **")

        elif (commands[0] not in self.valid_classes):
            print("** class doesn't exist **")

        elif (len(commands) < 2):
            print("** instance id missing **")

        else:
            objs = storage.all()

            key = "{}.{}".format(commands[0], commands[1])

            if (key in objs):
                del objs[key]
                storage.save()

            else:
                print("** no instance found **")

    def do_all(self, arg):
        '''
        Prints all string representation of all instances
        based or not on the class name.
        '''

        objs = storage.all()
        commands = shlex.split(arg)

        if (len(commands) == 0):
            for key, value in objs.items():
                print(str(value))

        elif (commands[0] not in self.valid_classes):
            print("** class doesn't exist **")

        else:
            for key, value in objs.items():
                if (key.split('.')[0] == commands[0]):
                    print(str(value))

    def do_update(self, arg):
        '''
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        '''

        commands = shlex.split(arg)

        if (len(commands) == 0):
            print("** class name missing **")

        elif (commands[0] not in self.valid_classes):
            print("** class doesn't exist **")

        elif (len(commands) < 2):
            print("** instance id missing **")

        else:
            objs = storage.all()
            key = "{}.{}".format(commands[0], commands[1])

            if (key not in objs):
                print("** no instance found **")

            elif (len(commands) < 3):
                print("** attribute name missing **")

            elif (len(commands) < 4):
                print("** value missing **")

            else:
                obj = objs[key]
                crl_braces = re.search("{{(.*?)}}", arg)

                if (crl_braces):
                    try:
                        str_data = crl_braces.group(1)
                        arg_dict = ast.literal_eval("{" + str_data + "}")

                        attr_names = list(arg_dict.keys())
                        attr_values = list(arg_dict.values())

                        try:
                            attr_name1 = attr_names[0]
                            attr_value1 = attr_values[0]
                            setattr(obj, attr_name1, attr_value1)
                        except Exception:
                            pass

                        try:
                            attr_name2 = attr_names[1]
                            attr_value2 = attr_values[1]
                            setattr(obj, attr_name2, attr_value2)
                        except Exception:
                            pass
                    except Exception:
                        pass

                else:
                    attr_name = commands[2]
                    attr_value = commands[3]

                    try:
                        attr_value = eval(att_value)
                    except Exception:
                        pass

                    setattr(obj, attr_name, attr_value)

                obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
