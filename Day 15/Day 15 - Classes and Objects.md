# Day 15 - Classes and Objects

# Table of Contents

# Classes and Objects

- Python is an object oriented programming language meaning everything in Python is an object, with its properties and methods
- To create an object, must first create a class
- A class is like an object constructor or a blueprint for creating objects
- When a class is instantiated an object is created
- The class defines attributes and behavior of the object, while the object represents the class
- to create a class, you need the key word class followed by the name and colon and class name should be CamelCase

```other
# syntax
class ClassName:
  code goes here
```

- create an object by calling the class
   - `c = ClassName()`
- a class without a constructor is not really useful in real applications
   - use the constructor function to make the class more useful
   - Python has a built-in init() constructor function
      - the init constructor function has self parameter which is a reference to the current instance of the class
      - can add more parameters to the constructor function

```other
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city


p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
```

- objects can have methods.
   - the methods are functions which belong to the object

```other
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'

p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.person_info())
```

- sometimes, you may want to have a default values for your object methods
   - giving default values for the parameters in the consructor can avoid errors when the class is called or instantiated without parameters

```other
class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
```

- can use methods to modify class default values by adding the method to the class

## Inheritance

- using inheritance, you can reuse parent class code
- Inheritance allows you to define a class that inherits all the methods and properties from parent class
- The parent class or super or base is the class which gives all the methods and properties
- The child class is the class that inherits from another

```other
class Student(Person):
    pass

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
print(s1.person_info())
```

- you do not have to call the init() constructor in the child class it can still access all the properties from the parent
   - if you do, you can access the parent properties by calling super
- can add a new method to the child or override the parent class methods by creating the same method name in the child class
- when an init() function is added the child class will no longer inherit the parent’s init() function

```other
class Student(Person):
    def __init__ (self, firstname='Asabeneh', lastname='Yetayeh',age=250, country='Finland', city='Helsinki', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname,age, country, city)
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki','male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
```

