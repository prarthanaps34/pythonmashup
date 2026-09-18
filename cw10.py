from abc import ABC, abstractmethod

class User(ABC):

    def __init__(self, name, joining_year):
        self.__name = name
        self.__joining_year = joining_year

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def joining_year(self):
        return self.__joining_year

    @joining_year.setter
    def joining_year(self, value):
        self.__joining_year = value

    def years_on_platform(self):
        return 2025 - self.__joining_year

    @abstractmethod
    def role(self):
        pass

    def __str__(self):
        return f"Name: {self.name}, Role: {self.role()}, Years on Platform: {self.years_on_platform()}"


class Customer(User):

    def role(self):
        return "Customer"


class Vendor(User):

    def role(self):
        return "Vendor"


customer = Customer("Priya", 2020)
vendor = Vendor("Navya", 2018)

print(customer)
print(vendor)