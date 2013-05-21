#! /usr/bin/python


class Animal(object):

    """docstring for Animal"""

    # private attribute
    __name = ""

    def __init__(self):
        super(Animal, self).__init__()

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


def main():
    queeny = Animal()
    queeny.set_name('Queeny')
    print queeny.get_name()


if __name__ == '__main__':
    main()
