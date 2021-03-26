"""
Sources:

https://www.youtube.com/watch?v=QaOdwYVp2ik
https://www.youtube.com/watch?v=EcFVTgRHJLM
https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_abstract_factory.htm

Description:

The factory method pattern has the intention to define an interface
for the creation of an object, allowing for the subclasses to decide
what kind of object to instaciate.

It is often applied when you can not known the type of the object you
have to instaciate or when you want to specify over the subclasses, of
the factory interface, how to instaciate the object.

Participants:
- Product: Common interface to all concrete product instanciation.
- ConcreteProduct: Concrete class that implements the @Product interface
- Creator (or Factory): Abstract class for the instanciation of
                        a @ConcreteProduct.
- ConcreteCreator (or ConcreteFactory): Subclass that implements the abstract
                        class @Creator overriding part of the creation of a
                        @ConcreteProduct.
"""


from abc import ABC, abstractmethod
from typing import List

class BaseModel(ABC):
    """[Product interface]"""

    def save(self):
        print("DB persisted")

class UserModel(BaseModel):
    """[Concrete Product]"""
    def __repr__(self) -> str:
        return "Result of the UserModel"

class GroupModel(BaseModel):
    """[Concrete Product]"""
    def __repr__(self) -> str:
        return "Result of the GroupModel"

class Factory(ABC):
    """[Creator] abstract class"""

    @abstractmethod
    def factory_method(self):
        pass

    def create(self) -> BaseModel:
        product = self.factory_method()
        product.save()
        return product

    def create_bacth(self, num) -> List[BaseModel]:
        result = []
        for i in range(num):
            product = self.factory_method()
            product.save()
            result.append(product)
        return result

class UserFactory(Factory):
    """[Concrete Creator]"""

    def factory_method(self) -> UserModel:
        return UserModel()

class GroupFactory(Factory):
    """[Concrete Creator]"""

    def factory_method(self) -> GroupModel:
        return GroupModel()