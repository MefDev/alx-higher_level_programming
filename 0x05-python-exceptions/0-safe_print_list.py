# print the numbers depening on the second argument
# try first then except
# use a for loop to print
# check if the i is less than x
# you don't need to use len you should use a counter instead

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
