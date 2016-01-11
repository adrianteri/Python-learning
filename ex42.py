## Animal is-a object (yes, sort of confusing) 
class Animal(object):
	pass

## Dog is-a Animal is-a object
class Dog(Animal):

    def __init__(self,name):
        ##
        self.name = name

## Cat is-a Animal is-a object
class Cat(Animal):

    def __init__(self,name):
        ##  Cat has-a name 
        self.name = name

## Person is-a object
class Person(object):
    
    def __init__(self,name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

##
class Employee(Person):
    def __init__(self, name, salary):
    	## hmm what strange magic?
    	super(Employee,self).__init__(name)
    	## Employee has-a salary
    	self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish is-a object
class Salmon(Fish):
    pass

## Halibut is-a Fish is-a object
class Halibut(Fish):
    pass

## rover is-a dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet named satan
mary.pet = satan

## frank is-a Employee and has-a salary of 120000
frank = Employee("Frank", 120000)

## frank has-a pet named rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## harry is-a halibut
harry = Halibut()

