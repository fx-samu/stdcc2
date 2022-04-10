"""
    Imports
"""
import os
import time
import colorama

"""
    Constants
"""
_function    = type(lambda: None)
_separator   = "\x10"

"""
    Color dict
"""

color       = {
	"0"		: "\033[39m",		 # RESET ALL
	"L"		: "\033[2J\033[1;1f",# 0 Cursor reset
	"O"     : "\033[0;30m",		 # O BLACK
	"R"     : "\033[0;31m", 	 # R RED
	"G"     : "\033[0;32m", 	 # G GREEN
	"Y"     : "\033[0;33m",		 # Y YELLOW
	"B"     : "\033[0;34m", 	 # B BLUE
	"P"     : "\033[0;35m",		 # P PURPLE
	"C"     : "\033[0;36m",		 # C CYAN
	"W"     : "\033[0;37m", 	 # W WHITE
	"o"     : "\033[1;30m", 	 # o black
	"r"     : "\033[1;31m",		 # r red
	"g"     : "\033[1;32m", 	 # g green
	"y"     : "\033[1;33m", 	 # y yellow
	"b"     : "\033[1;34m", 	 # b blue
	"p"     : "\033[1;35m", 	 # p purple
	"c"     : "\033[1;36m",		 # c cyan
	"w"     : "\033[1;37m",		 # w white
}


"""
    Lambda Function
"""
_time = lambda: time.strftime("%m/%d/%Y @ %H:%M:%S >>", time.localtime())
_version = lambda: "0.0.1"

"""
    Functions
"""
def f_name (name: str, func:_function) -> None:
    """
    Function to change the name of a function
    on the __code__ object by adding it as a prefix separated by a slash
    """
    # check the types of the arguments
    _TypeChecks([name, func], [str, function])
    func.__code__ = func.__code__.replace(co_name="{}/{}".format(name, func.__code__.co_name))

def log(*args, **kwargs):
    """
    A replacement of print
    """

"""
    Private Functions
"""
def _TypeChecks(objs: list, types: list):
    """
    Function to check if objs are from the instance types of types
    and if it isn't it will raise an error
    """
    for obj, type in zip(objs, types):
        if not isinstance(obj, type):
            raise TypeError("{} is not of type {}".format(obj, type))

def _format(*args):
    """
    Function format
    gets a random list of objects which are converted to strings
    then using _separator as a flag will use the character next to it as a key for the "color" dict and will replace it for it's value
    then returns the lists as one single string separated by spaces
    """
    # Convert all items in args into strings
    args = [str(arg) for arg in args]
    
    # for each item in args
    for i in range(len(args)):
        if args[i]:
            lstr = list(args[i])
            n = len(lstr)
            lstr.append(_separator)
            j = 0
            while True:
                if lstr[j] == _separator:
                    if j >= n-1:
                        if j == n-1:
                            lstr[n-1] = ""
                        lstr[n] = ""
                        break
                    lstr[j] = color.get(lstr[j+1], "")
                    lstr[j+1] = ""
                    j += 1
                j += 1
            args[i] = "".join(lstr)
    return " ".join(args)

"""
    Main function
"""
def _init():
    """
    Function to initialize the program
    """
    # Initialize colorama
    colorama.init()
    print(_version())
_init()
def _main():
    print(_format(1,2,"a\x10\x10 \x10", "\x10rHello World\x10gHello World"))
if __name__ == "__main__": _main()