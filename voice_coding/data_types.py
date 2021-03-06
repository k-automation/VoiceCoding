from voice_coding.helpers.format_var_func_name import format_var_func_name
from voice_coding.helpers.text2num import text2num
from voice_coding.helpers.convert_list_vals import convert_list_vals
from voice_coding.helpers.to_builtin import to_builtin
from voice_coding.helpers.voice_conversion import voice_conversion
from voice_coding.helpers.get_method import get_method
from voice_coding.helpers.get_params import get_params
from voice_coding.code_class import Code


# checks and returns the data type
def verify(val, val_type=None):
    # checks if there is a method, returns it, and modifies val
    method = get_method(val)
    val = voice_conversion(val, "method").replace(method[1], "").rstrip()
    # checks for assumed data types (int, float, bool, str) if no data is named
    if val_type is None:
        for i in assumed_data_types:
            if i(val) is False:
                pass
            else:
                return "{0}{1}".format(i(val), method[0])
    # check for data type if data type is named
    if val_type in data_types:
        return "{0}{1}".format(data_types[val_type](val), method[0])
    else:
        return False


# formats the data type according what type it is; used by the commands
def format_value(val):
    val = val.strip()
    # checks if data type is named
    try:
        data_type = val.split()[0].lower()
        data_type = voice_conversion(val.split()[0].lower(), "data_type")
    except:
        data_type = None
    # verifies a named data type
    if data_type in data_types:
        data_value = " ".join(val.split()[1:])
        var_val = verify(data_value, data_type)
    else:
        var_val = verify(val)
    # checks if a data type was returned
    if var_val is False:
        return False
    else:
        return var_val


# returns a string
def check_str(val):
    if val == "space":
        val = " "
    return '"{0}"'.format(val)


# returns an integer
def check_int(val):
    # converts words to numbers
    try:
        val = text2num(val)
    except:
        pass
    # checks if val is an integer
    try:
        int_val = int(val)
        return int_val
    except ValueError:
        return False


# returns a float
def check_float(val):
    val = val.replace("point", ".")
    parts = val.split(".")
    try:
        # convert whole number words to a number
        parts[0] = str(text2num(parts[0]))
        # convert decimal words to a number
        parts[1] = str(text2num(parts[1]))
    except:
        pass
    try:
        # joins whole number and decimal together
        val_float = float(".".join(parts))
        return val_float
    except:
        return False


# returns a boolean
def check_bool(val):
    if val.lower() == "false":
        return "False"
    elif val.lower() in ["true", "through", "tru"]:
        return "True"
    else:
        return False


# returns a variable
def check_var(val):
    # formats variable name to snake_case
    variable = format_var_func_name(val)
    if not variable:
        return False
    else:
        return variable


# returns a variable; run when "variable" is not said
def check_var_assumed(val):
    variable = format_var_func_name(val)
    if not variable:
        return False
    else:
        # makes sure variable has been defined already
        if variable not in Code.defined_vars:
            return False
        else:
            return variable


# returns an equation
def check_equation(val):
    # maps words to an operation
    operations = {"plus": "+",
                  "Plus": "+",
                  "+ ": " + ",
                  " +": " + ",
                  "minus": "-",
                  "times": "*",
                  "multiplied by": "*",
                  "divided by": "/",
                  "over": "/",
                  "to the power of": "**",
                  "modulus": "%",
                  "mod": "%",
                  "madh": "%",
                  "made": "%",
                  "iPod": "i %"}

    # replaces words that map to an operation
    for i in operations:
        val = val.replace(i, operations[i])
    if "variable X" not in val and "variable x" not in val:
        val = val.replace(" x ", " * ")
        val = val.replace(" X ", " * ")

    # keeps track of operations that are being used
    eq_operations = [i for i in val.split() if i in operations.values()]
    if len(eq_operations) == 0:
        return False

    # converts the operands to data types and formats them with the operations
    operands = val
    for i in eq_operations:
        operands = operands.replace(i, "(@!@)")

    operand_dict = {}
    for i in operands.split("(@!@)"):
        operand_dict[i] = format_value(i)

    if False in operand_dict.values():
        return False

    for i in operand_dict:
        val = val.replace(i, str(operand_dict[i]))

    if val is False:
        return False
    else:
        return "({0})".format(val)


# returns a comparison expression
def check_comp(val):
    # maps words to comparisons
    comparisons = {"equals": "==",
                   "is equal to": "==",
                   "is equals to": "==",
                   "does not equal": "!=",
                   "does not equals": "!=",
                   "is not equal to": "!=",
                   "is not equals to": "!=",
                   "is greater than": ">",
                   "is less than": "<",
                   "is greater than or equal to": ">=",
                   "is greater than or equals to": ">=",
                   "is less than or equal to": "<=",
                   "is less than or equals to": "<="}

    word_comparisons = {"and": "and",
                        "hand": "and",
                        "not": "not",
                        "or": "or",
                        "is": "is",
                        "in": "in"}

    # replaces words that map to a comparison
    for i in comparisons:
        val = val.replace(i, comparisons[i])
    for i in word_comparisons:
        val = val.replace(i, word_comparisons[i])
    val = val.replace("equal", "==")

    # keeps track of the comparison operators being used
    comp_ops = [i for i in val.split() if i in comparisons.values() or
                i in word_comparisons.values()]

    # converts the objects being compared to valid data types
    # and formats them with the comparison operators
    to_compare = val
    for i in comp_ops:
        to_compare = to_compare.replace(i, "(@!@)")

    to_compare_dict = {}
    for i in to_compare.split("(@!@)"):
        to_compare_dict[i] = format_value(i)

    if False in to_compare_dict.values():
        return False

    for i in to_compare_dict:
        val = val.replace(i, " {0} ".format(str(to_compare_dict[i])))

    return "{0}".format(val.rstrip().lstrip())


# returns a list
def check_list(val):
    list_items = val.split("cut")
    l = convert_list_vals(list_items)
    if l is False:
        return False
    else:
        return "{0}".format(l)


# returns a tuple
def check_tuple(val):
    tuple_items = val.split("cut")
    t = convert_list_vals(tuple_items)
    if t is False:
        return False
    else:
        if t == []:
            return "()"
        # if there is only one object in the tuple, add a "," at the end
        elif "," not in t:
            return "{0}{1}{2}".format("(", t[1:-1], ",)")
        else:
            return "{0}{1}{2}".format("(", t[1:-1], ")")


# returns a set
def check_set(val):
    set_items = val.split("cut")
    s = convert_list_vals(set_items)
    if s is False:
        return False
    else:
        # if the set it empty return the `set()` function
        if s == []:
            return "set()"
        else:
            return "{0}{1}{2}".format("{", s[1:-1], "}")


# returns a function
def check_func(val):
    val = voice_conversion(val, "function")
    parameters = get_params(val)
    function_name = val.split("parameters")[0]

    # attempts to make function a Python builtin
    if to_builtin(function_name):
        function_name = to_builtin(function_name)
    else:
        # formats the name as snake_case if it is not a builtin
        function_name = format_var_func_name(function_name.rstrip())
    if parameters is False:
        return False
    else:
        return "{0}{1}".format(function_name, parameters)

# data types that don't need to be explicitly named
assumed_data_types = [check_var_assumed,
                      check_int,
                      check_float,
                      check_bool,
                      check_str]

# all data types
data_types = {"string": check_str,
              "integer": check_int,
              "float": check_float,
              "boolean": check_bool,
              "variable": check_var,
              "equation": check_equation,
              "comparison": check_comp,
              "list": check_list,
              "tuple": check_tuple,
              "set": check_set,
              "function": check_func}
