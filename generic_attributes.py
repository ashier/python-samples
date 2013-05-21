#! /usr/bin/python


class Animal(object):

    """docstring for Animal"""

    # private attribute
    __name = ""
    __dictAttr = []

    # init method
    def __init__(self, **kvargs):
        super(Animal, self).__init__()
        self._attributes = kvargs

     # getter/setters
    def set_attribute(self, key, value):
        self._attributes[key] = value

    def get_attribute(self, key):
        return self._attributes[key]


def main():
    queeny = Animal(Name='Queeny', Age='1.2')
    print queeny.get_attribute('Name')
    print queeny.get_attribute('Age')


if __name__ == '__main__':
    main()
