#!/usr/bin/python3

"""A MyList Class Module """


class MyList(list):
    """A derived class of the list class

    """
    def print_sorted(self):
        """A function that prints the sorted copy of a list in ascending order

        """
        print(sorted(self))
