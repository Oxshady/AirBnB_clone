#!/usr/bin/python3
import shlex
import cmd as cmd_hbnb
from sys import stdin
from models.base_model import BaseModel as B_S
from models import storage as st
classes = {
	"BaseModel": B_S,
}
class HBNBCommand(cmd_hbnb.Cmd):
    prompt = "(hbnb)"

    def do_EOF(self, line):
        return True

    def help_EOF(self):
        print("EOF command to exit the program")
    do_quit = do_EOF
    def help_quit(self):
        print("Quit command to exit the program")

    def emptyline(self):
        pass
    def do_create(self, nedded_class):
        if not nedded_class:
            print("** class name missing **")
            return
        if nedded_class not in classes:
            print("** class doesn't exist **")
            return
        created = B_S()
        created.save()
        print(created.id)
    def do_show(self, arg):
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
            tmp = B_S(**(objects[s]))
            print(tmp.__str__())
    def do_destroy(self, arg):
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
        objects = st.all()
        if not arg:
            tmp = list()
            for key in objects:
                tmp.append(B_S(**objects[key]).__str__())
            print(tmp)
        else:
            if arg not in classes:
                print("** class doesn't exist **")
                return
            tmp = list()
            for key in objects:
                a = key.split(".")
                if a[0] == arg:
                    tmp.append(B_S(**objects[key]).__str__())
            if tmp:
                print(tmp)
                
if __name__ == "__main__":
    if stdin.isatty():
        HBNBCommand().cmdloop()
    else:
        for command in stdin:
            HBNBCommand().onecmd(command.strip())