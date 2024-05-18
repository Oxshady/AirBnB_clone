#!/usr/bin/python3
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
	"BaseModel": B_S
    ,"User": uS
    ,"Amenity": A
    ,"City": cCc
    ,"State": s_s
    ,"Review": RrR
    ,"Place": PpP
}
class HBNBCommand(cmd_hbnb.Cmd):
    prompt = "(hbnb)"
    st.reload()
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
        created = classes[nedded_class]()
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
            tmp = classes[args[0]](**(objects[s]))
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
                a = key.split(".")
                tmp.append(classes[a[0]](**objects[key]).__str__())
            print(tmp)
        else:
            if arg not in classes:
                print("** class doesn't exist **")
                return
            tmp = list()
            for key in objects:
                a = key.split(".")
                if a[0] == arg:
                    tmp.append(classes[a[0]](**objects[key]).__str__())
            if tmp:
                print(tmp)
    def do_update(self,arg):
        args = shlex.split(arg)
        lenght = len(args)
        if not lenght:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("class dosen't exist")
            return
        if lenght < 2:
            print("** instance id missing **")
            return
        objects = st.all()
        c_id = ".".join([args[0],args[1]])
        if objects.get(c_id) is not None:
            if lenght < 3:
                print("** attribute name missing **")
                return
            if lenght < 4:
                print("** value missing **")
                return
            if args[3] in ["updated_at","created_at","id"]:
                return
            ob = classes[args[0]](**objects[c_id])
            setattr(ob,args[2],args[3])
            objects[c_id] = ob.to_dict()
            st.save()
if __name__ == "__main__":
    if stdin.isatty():
        HBNBCommand().cmdloop()
    else:
        for command in stdin:
            HBNBCommand().onecmd(command.strip())