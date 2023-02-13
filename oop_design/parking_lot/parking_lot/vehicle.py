from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, license_no) -> None:
        self.__license_no = license_no

    @abstractmethod
    def assign_ticket(self, ticket):
        pass
