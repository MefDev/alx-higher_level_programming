#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "None"
    finally:
        if (result is None):
            print("Inside result: None")
        else:
            print("Inside result: {:.1f}".format(result))
