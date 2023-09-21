#!/usr/bin/python3
""" 14-main """
from base import Base
from rectangle import Rectangle

if __name__ == "__main__":

    json_dictionary = Base.to_json_string([])
    print(json_dictionary)
    print(type(json_dictionary))