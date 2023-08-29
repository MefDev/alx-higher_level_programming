#!/usr/bin/python3
def safe_function(fct, *args):
    a = args[0]
    b = args[1]
    try:
        div = fct(a, b)
        return div
    except (ZeroDivisionError, IndexError, TypeError, ValueError) as err:
        print("Exception: {}".format(err))
        return None
   
