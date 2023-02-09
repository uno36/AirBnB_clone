# This project describe the making of AirBnB clone

The cmd module contains one public class, Cmd, designed to be used as a base class for command processors such as interactive shells and other command interpreters. By default it uses readline for interactive prompt handling, command line editing, and command completion.

## Processing Commands
The interpreter uses a loop to read all lines from its input, parse them, and then dispatch the command to an appropriate command handler. Input lines are parsed into two parts. The command, and any other text on the line. If the user enters a command ==foo bar==, and your class includes a method named **do_foo()**, it is called with =="bar"== as the only argument.

The end-of-file marker is dispatched to **do_EOF(**). If a command handler returns a true value, the program will exit cleanly. So to give a clean way to exit your interpreter, make sure to implement **do_EOF(**) and have it return True.

~~~~
This simple example program supports the “greet” command:

import cmd

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""

    def do_greet(self, line):
        print "hello"

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()
~~~~

