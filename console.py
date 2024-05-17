#!/usr/bin/python3
import cmd as cmd_hbnb
from sys import stdin


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


if __name__ == "__main__":
    if stdin.isatty():
        HBNBCommand().cmdloop()
    else:
        for command in stdin:
            HBNBCommand().onecmd(command.strip())
