#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    length = 0
    try:
        for i in my_list:
            length += 1
        count = 0
        for i in range(length):
            if i < x:
                print(my_list[i], end="")
                count += 1
        print()
        return count
    except IndexError as IndexErr:
        print("Index error there", IndexErr)
    except TypeError as typeErr:
        print("Type error there", typeErr)
