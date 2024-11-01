import random

class Animal(object):

    def __init__(self, name):
        self.name = name

class Dog(Animal):

    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.breed = random.choice(['Shih Tzu', 'Beagle', 'Mutt'])

    def fetch(self, thing):
        print('%s goes after the %s!' % (self.name, thing))


d = Dog('Ollie')
print(d.name)
print(d.breed)