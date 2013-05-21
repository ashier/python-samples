#! /usr/bin/python


class Animal(object):

    """docstring for Animal"""

    # private attribute
    __name = "No Name"

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


def playPet(Animal):
    print Animal.get_attribute('Name')
    Animal.talk()


def main():
    queeny = Animal(Name='Queeny')
    tweety = Bird(Name='Tweety')
    playPet(queeny)
    playPet(tweety)


if __name__ == '__main__':
    main()
