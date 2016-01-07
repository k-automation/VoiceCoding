from voice_coding.command_functions.assign_variable import assign_variable
from voice_coding.command_functions.print_data import print_data
from voice_coding.command_functions.call_func_method import call_func_method
from voice_coding.command_functions.if_else import if_else
from voice_coding.command_functions.for_loop import for_loop
from voice_coding.command_functions.while_loop import while_loop
from voice_coding.command_functions.def_func import def_func
from voice_coding.command_functions.return_func import return_func

# commands that can be called by the user; the first word in the voice command
instructions = {"assign": assign_variable,
                "print": print_data,
                "call": call_func_method,
                "if": if_else,
                "for": for_loop,
                "while": while_loop,
                "define": def_func,
                "return": return_func}
