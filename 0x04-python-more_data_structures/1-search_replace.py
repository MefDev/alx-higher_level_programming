#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    return ("".join(str(new_list).replace(str(search), str(replace))))
