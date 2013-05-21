#! /usr/bin/python


class Animal(object):

    """docstring for Animal"""

    # private attribute
    __name = ""

    # init method
    def __init__(self, **kvargs):
        super(Animal, self).__init__()
        self._attributes = kvargs

    # getter/setters
    def set_attribute(self, key, value):
        self._attributes[key] = value

    def get_attribute(self, key):
        return self._attributes[key]

    def talk(self):
        print 'Hi'


class Bird(Animal):

    def __init__(self, **kvargs):
        # Inherit parent attributes
        super(Bird, self).__init__()
        self._attributes = kvargs

    # Overriding parent method "talk"
    def talk(self):
        print 'Tweet tweet'
        # Access parent talk
        # Animal.talk(self, 'Tweet tweet')


def main():
    queeny = Animal(Name='Queeny', Age='1.2')
    print queeny.get_attribute('Name')
    print queeny.get_attribute('Age')
    print queeny.talk()

    tweety = Bird(Name='Tweety', Age='.3')
    print tweety.get_attribute('Name')
    print tweety.get_attribute('Age')
    print tweety.talk()


if __name__ == '__main__':
    main()
