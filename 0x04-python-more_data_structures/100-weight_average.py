#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sum = 0
    substructBy = 0
    average = 0
    new_list = my_list.copy()
    for tuples in new_list:
        new_little_list = list(tuples)
        sum += new_little_list[0] * new_little_list[1]
    for tuples in range(len(my_list)):
        substructBy += my_list[tuples][1]
    average = sum / substructBy
    return average
