
def safe_function(fct, *args):
    a = args[0]
    b = args[1]
    try:
        div = fct(a, b)
        return div
    except ZeroDivisionError as divErr:
        print("Exception: {}".format(divErr))
        return None
    except IndexError as indxErr:
        print("Exception: {}".format(indxErr))
        return None
