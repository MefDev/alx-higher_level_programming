#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for i in new_list:
        index = new_list.index(search)
        if index in new_list:
            new_list[index] = replace
        else:
            return new_list
    return new_list
