#!/user/bin/python3

from abc import ABC, abstractmethod
from datetime import date

class AbstractClassExample(ABC):

    @abstractmethod
    def generate_age(self, name, birth_year):
        pass

    @abstractmethod
    def print_info_factory_method(self):
        pass


class ConcreteClassExample(AbstractClassExample):

    # Class variables
    current_objective = "Get a new job"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def generate_age(cls, name, birth_year):
        return cls(name,date.today().year - birth_year)

    @classmethod
    def show_objective(cls):
        print(ConcreteClassExample.current_objective)

    def print_info_factory_method(self):
        print(f"{self.name}'s age is {self.age}")

    @staticmethod
    def get_higher_value(x, y):
        return max(x, y)


# Create object with precalculated age
tyler = ConcreteClassExample('Tyler', 39)
tyler.print_info_factory_method()


# Create factory with class method using birth year, leaving implementation detail inside the class
other_applicant = ConcreteClassExample.generate_age('Bob', 1984)
other_applicant.print_info_factory_method()


# Access class variable without an instance
ConcreteClassExample.show_objective()


# Use utility static method
print(tyler.get_higher_value(500,1000))
