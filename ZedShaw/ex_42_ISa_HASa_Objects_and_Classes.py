# Python - The Hard Way - Exercise 42 - Is-A, Has-A, Objects & Classes

# Animal is-a object
class Animal(object):
    pass

# is-a Animal
class Dog(Animal):

    def __init__(self, name):
        #??
        self.name = name

# is-a Aninimal
class Cat(Animal):

    def __init__(self, name):
        #??
        self.name = name

# is-a Object
class Person(object):

    def __init__(self, name):
        #has-a __init__ that takes self, name
        self.name = name

        #person has-a pet of some kind
        self.pet = None

# class empoyee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        #??
        super(Employee, self).__init__(name)
        #??
        self.salary = salary

# is-a object
class Fish(object):
    pass

# is-a Fish
class Salmon(Fish):
    pass

# is-a Fish
class Halibut(Fish):
    pass

# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# mary is-a Person
mary = Person("Mary")

# mary has-a pet(satan)
mary.pet = satan

# set frank as an instance of an Employee with argements self, "Frank", and 120000
frank = Employee("Frank", 120000)

# frank has-a pet(rover)
frank.pet = rover

# flipper is-a Fish
flipper = Fish()

# crouse is-a instance of a class Salmon
crouse = Salmon()

# harry is-a instance of class Halibut
harry = Halibut()
