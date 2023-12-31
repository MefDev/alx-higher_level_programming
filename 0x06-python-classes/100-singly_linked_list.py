#!/usr/bin/python3
"""
creates a node class object
"""


class Node:
    """
    Represents a node object.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a node object.

        Args:
            data (int): Data value of the node.
            next_node (Node): Reference to the next node. Defaults to None.

        Raises:
            TypeError: If data is not an integer.
            TypeError: If next_node is not a Node object or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):

        return self.__data

    @data.setter
    def data(self, value):

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, (Node, type(None))):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""
creates a singly linked list class object
"""


class SinglyLinkedList:
    """
    Represents a singly linked list object.
    """

    def __init__(self):

        self.__head = None

    def __str__(self):

        new_list = []
        current_node = self.__head
        while current_node:
            new_list.append(current_node.data)
            current_node = current_node.next_node
        return "\n".join(str(x) for x in sorted(new_list))

    def sorted_insert(self, value):

        new_node = Node(value, self.__head)
        self.__head = new_node
