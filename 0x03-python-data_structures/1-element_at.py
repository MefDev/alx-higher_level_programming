#!/usr/bin/python3
if __name__=="__name__":
    def element_at(my_list, idx):
        if idx < 0 or idx > len(my_list):
            return "None"
        else:
            return my_list[idx]
