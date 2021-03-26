"""
Abstract classes are classes that contain one or more abstract methods.
An abstract method is a method that is declared, but contains no
implementation. 

Abstract classes cannot be instantiated, and require subclasses to
provide implementations for the abstract methods.

From: https://www.python-course.eu/python3_abstract_classes.php

Notes:
Seems pretty much like interfaces
"""

from abc import ABC, abstractmethod
 
class AbstractClassExample(ABC):
 
    def __init__(self, value):
        self.value = value
        super().__init__()
    
    @abstractmethod
    def do_something(self):
        pass


class DoAdd42(AbstractClassExample):

    def do_something(self):
        return self.value + 42


x = DoAdd42(10)  # All good

"""
A class that is derived from an abstract class cannot be instantiated unless all of its abstract methods are overridden.

You may think that abstract methods can't be implemented in the abstract base class. This impression is wrong: An abstract method can have an implementation in the abstract class! Even if they are implemented, designers of subclasses will be forced to override the implementation. Like in other cases of "normal" inheritance, the abstract method can be invoked with super() call mechanism. This enables providing some basic functionality in the abstract method, which can be enriched by the subclass implementation.
"""

class AbstractClassExample(ABC):
    
    @abstractmethod
    def do_something(self):
        print("Some implementation!")
        
class AnotherSubclass(AbstractClassExample):

    def do_something(self):
        super().do_something()
        print("The enrichment from AnotherSubclass")
        
x = AnotherSubclass()
x.do_something()

"""
Here it is visible that abstract methods in abstract class can be implemented,
and if that is the case, it could not fullfil the "interface" concept.
"""