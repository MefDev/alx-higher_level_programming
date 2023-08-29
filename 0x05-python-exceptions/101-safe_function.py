#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    if (len(args) < 2):
        print("Exception: Not enough arguments provided")
    else:
        a = args[0]
        b = args[1]
    try:
        div = fct(a, b)
        return div
    except (ZeroDivisionError, IndexError) as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return None
