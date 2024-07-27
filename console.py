#!/usr/bin/python3
"""The `HBNBCommand` class provides a console interface
for creating, updating, and destroying objects
of various classes in a Python application."""

import shlex
import cmd as cmd_hbnb
from sys import stdin
from models.base_model import BaseModel as B_S
from models import storage as st
from models.user import User as uS
from models.amenity import Amenity as A
from models.city import City as cCc
from models.state import State as s_s
from models.review import Review as RrR
from models.place import Place as PpP

classes = {
    "BaseModel": B_S,
    "User": uS,
    "Amenity": A,
    "City": cCc,
    "State": s_s,
    "Review": RrR,
    "Place": PpP,
}


class HBNBCommand(cmd_hbnb.Cmd):
    """The `HBNBCommand` class defines methods for creating,
    showing, destroying, listing, and updating
    instances in a program."""

    prompt = "(hbnb)"
    st.reload()

    def do_quit(self, line):
        """
        The `do_quit` function returns `True` when called.

        :param line: The `do_EOF` method you provided seems
        to be a part of a class or a script that
        handles input. The `do_EOF` method is typically
        used to handle the end-of-file signal,
        indicating the end of input. In this case,
        the method simply returns `True`
        :return: True
        """
        print(self.prompt)
        return True

    def do_EOF(self, line):
        """
        The `do_EOF` function returns `True` when called.

        :param line: The `do_EOF` method you provided seems
        to be a part of a class or a script that
        handles input. The `do_EOF` method is typically
        used to handle the end-of-file signal,
        indicating the end of input. In this case,
        the method simply returns `True`
        :return: True
        """
        print("")
        exit()

    def help_EOF(self):
        """
        The function `help_EOF` prints a message explaining
        the EOF command to exit the program.
        """
        print("EOF command to exit the program")

    def help_quit(self):
        """
        The function `help_quit` prints a message about
        the Quit command to exit the program.
        """
        print("Quit command to exit the program")

    def emptyline(self):
        """
        The function "emptyline" does not contain
        any code and simply passes.
        """
        pass

    def do_create(self, nedded_class):
        """
        The function `do_create` creates an instance
        of a specified class and prints its ID.

        :param nedded_class: The `nedded_class` parameter
        in the `do_create` method is used to specify
        the class name of the object that needs to be created.
        This method checks if the `nedded_class`
        is provided, if it exists in the `classes` dictionary,
        creates an instance of that class,
        :return: The `do_create` method returns the `id` of
        the created instance after saving it.
        """
        if not nedded_class:
            print("** class name missing **")
            return
        if nedded_class not in classes:
            print("** class doesn't exist **")
            return
        created = classes[nedded_class]()
        created.save()
        print(created.id)

    def do_show(self, arg):
        """
        The function `do_show` takes an argument, checks if a
        class and instance exist, and prints the
        string representation of the instance if found.

        :param arg: The `arg` parameter in the `do_show` method
         is a string that represents the
        arguments passed to the method. It is then split using
        the `shlex.split()` function to separate
        the arguments. The method checks if the necessary arguments
         are present and performs various
        checks based on the arguments provided
        :return: The `do_show` method is returning the string
        representation of the instance object
        `tmp` by calling its `__str__` method.
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        else:
            if args[0] not in classes:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            s = ".".join(args)
            objects = st.all()
            if s not in objects.keys():
                print("** no instance found **")
                return
            print(objects[s].__str__())

    def do_destroy(self, arg):
        """
        The function `do_destroy` takes an argument,
         checks if a class and instance exist, and deletes
        the instance if found.

        :param arg: The `arg` parameter in the `do_destroy`
         method is a string that represents the
        arguments passed to the method. It is then split using
         the `shlex.split()` function to separate
        the arguments. The method checks for the presence of
        a class name, instance id, and the
        existence of the
        :return: The `do_destroy` method is returning None.
        This is because there is no explicit return
        statement at the end of the method. If none of the conditions
        are met and the method completes
        execution without encountering a return statement,
         it will implicitly return None.
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        s = ".".join(args)
        objects = st.all()
        if s not in objects.keys():
            print("** no instance found **")
            return
        del objects[s]
        st.save()

    def do_all(self, arg):
        """
        This function retrieves and prints objects based

        on a specified class or all classes if no
        argument is provided.

        :param arg: The `arg` parameter in the `do_all`

         method is used to filter the objects based on a
        specific class name. If `arg` is provided, the

        method will only print objects that belong to the
        specified class. If `arg` is not provided

         (empty or None), the method will
        :return: The `do_all` method is returning a

        list of string representations of objects that match
        the specified class name `arg`. If the `arg`

         is not provided or does not match any existing
        class, it will print "** class doesn't exist

        **" and return without any further action.
        """
        objects = st.all()
        if not arg:
            tmp = list()
            for key in objects:
                tmp.append(objects[key].__str__())
            print(tmp)
        else:
            if arg not in classes:
                print("** class doesn't exist **")
                return
            tmp = list()
            for key in objects:
                k = key.split(".")
                if k[0] == arg:
                    tmp.append(objects[key].__str__())
            if tmp:
                print(tmp)

    def do_count(self, arg):
        """
        This function retrieves the number of objects
        """
        objects = st.all()
        tmp = 0
        if not arg:
            for key in objects.keys():
                tmp += 1
            print(tmp)
        else:
            if arg not in classes:
                print("** class doesn't exist **")
                return
            for key in objects:
                k = key.split(".")
                if k[0] == arg:
                    tmp += 1
            print(tmp)

    def default(self, line: str) -> None:
        """
        implement dynamic commands
        """
        tmp = line.split(".")
        if tmp[0] in classes:
            if tmp[1] == "all()":
                self.do_all(tmp[0])
            if tmp[1] == "count()":
                self.do_count(tmp[0])

    def do_update(self, arg):
        """
        This function updates an attribute value of
         an instance of a class in a storage system.

        :param arg: The `do_update` method you
         provided seems to be a part of a class that handles
        updating instances of certain classes. The `arg`
         parameter is expected to be a string containing
        the necessary information for updating an instance.
        It should include the class name, instance
        id, attribute name, and the new
        :return: If the condition `if args[3] in
        ["updated_at","created_at","id"]` is met, then the
        function will return without performing any further actions.
        """
        args = shlex.split(arg)
        lenght = len(args)
        if not lenght:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if lenght < 2:
            print("** instance id missing **")
            return
        objects = st.all()
        c_id = ".".join([args[0], args[1]])
        if objects.get(c_id) is not None:
            if lenght < 3:
                print("** attribute name missing **")
                return
            if lenght < 4:
                print("** value missing **")
                return
            if args[3] in ["updated_at", "created_at", "id"]:
                return
            ob = objects[c_id]
            setattr(ob, args[2], args[3])
            objects[c_id] = ob
            st.save()
        else:
            print("** no instance found **")
            


if stdin.isatty():
    HBNBCommand().cmdloop()
else:
    for command in stdin:
        HBNBCommand().onecmd(command.strip())
