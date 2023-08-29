#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        div = fct(*args)
        return div
    except (ZeroDivisionError, IndexError) as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return None
