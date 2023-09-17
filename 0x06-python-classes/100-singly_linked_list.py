"""
A module implementing a singly linked list data structure using python
"""


class Node:
    """ A node implementation for a linked list

    Args:
        data(int): Integer value to be saved in the node
        next_node(Node): Node object or None

    Raises:
        TypeError: When the wrong data type is inputted. i.e. if data != int
                    or next_node != None or a Node object
    """
    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        """:obj:int: Getter for the data variable

        The setter sets the new data

        Args:
            value(int): The new data
        Raises:
            TypeError: If the value isn't an integer
        """
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """:obj:Node: Getter for the next_node variable

                The setter sets the next_node

                Args:
                    value(Node): The next node or None
                Raises:
                    TypeError: If the next node isn't a Node object or None
                """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    A class implementation of singly list data structure
    """
    def __init__(self):
        self.__head = None
        self.__temp = None

    def sorted_insert(self, value):
        """ A function that adds Nodes to the list

        Args:
            value(int): Data to be inserted into new node

        Raises:
            TypeError: Raises a type error if value isn't an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        new_node = Node(value)
        if self.__head is None:
            self.__head = self.__temp = new_node
        else:
            self.__temp.next_node = new_node
            self.__temp = new_node

    def __str__(self):
        """ A special function implementing the default action for when an
        object from this class is printed.

        :return:
            A string of values in the implemented class
        """
        self.__my_list = []
        self.__looper = self.__head
        while self.__looper:
            self.__my_list.append(self.__looper.data)
            self.__looper = self.__looper.next_node
        self.__new_list = sorted(self.__my_list)
        return "\n".join(map(str, self.__new_list))
