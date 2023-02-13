from abc import ABC, abstractmethod
from vehicle import Vehicle

class ParkingSpot(ABC):
    def __init__(self, id: str, isFree: bool, vehicle: Vehicle) -> None:
        self.__id = id
        self.__isFree = isFree
        self.vehicle = vehicle

    def is_free(self) -> bool:
        pass

    @abstractmethod
    def assign_vehicle(self, vehicle: Vehicle) -> None:
        pass

    def remove_vehicle(self):
        pass


