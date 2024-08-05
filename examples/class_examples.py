#!/user/bin/python3

from abc import ABC, abstractmethod
from datetime import date

class AbstractClassExample(ABC):

    # Require all child classes to have this method
    @abstractmethod
    def generate_age(self, name, birth_year):
        pass

    @abstractmethod
    def print_info_method(self):
        pass

# A class with all methods defined and no abstract methods
class ConcreteClassExample(AbstractClassExample):

    # Class variables
    current_objective = "Get a new job"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method bound to a class rather than an object and has access to class state
    @classmethod
    def generate_age(cls, name, birth_year):
        return cls(name,date.today().year - birth_year)

    @classmethod
    def show_objective(cls):
        print(ConcreteClassExample.current_objective)

    def print_info_method(self):
        print(f"{self.name}'s age is {self.age}")

    # Method bound to a class rather than an object and doesn't require instantiation
    @staticmethod
    def get_higher_value(x, y):
        return max(x, y)


# Create object with precalculated age
tyler = ConcreteClassExample('Tyler', 39)
tyler.print_info_method()


# Use class method
other_applicant = ConcreteClassExample.generate_age('Bob', 1984)
other_applicant.print_info_method()


# Access class variable without an instance
ConcreteClassExample.show_objective()


# Use static method without instance
print(tyler.get_higher_value(500,1000))
