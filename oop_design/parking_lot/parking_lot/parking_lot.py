from abc import ABC, abstractmethod
from vehicle import Vehicle


class ParkingLot(ABC):
    @abstractmethod
    def fee_calculator(self, vehicle: Vehicle):
