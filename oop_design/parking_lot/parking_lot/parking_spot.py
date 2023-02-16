from abc import ABC, abstractmethod
from vehicle import Vehicle
import uuid


class ParkingSpot(ABC):
    def __init__(self, id: str, is_free: bool, vehicle: Vehicle) -> None:
        self.__id = self.generate_id()
        self.__is_free = is_free
        self.vehicle = vehicle

    def generate_id(self):
        return uuid.uuid1()

    def is_free(self) -> bool:
        pass

    @abstractmethod
    def assign_vehicle(self, vehicle: Vehicle) -> None:
        pass

    def remove_vehicle(self):
        pass


class Motorcycle(ParkingSpot):
    def __init__(self, id: str, is_free: bool, vehicle: Vehicle) -> None:
        super().__init__(id, is_free, vehicle)

    def assign_vehicle(self, vehicle: Vehicle) -> None:
        pass


class Large(ParkingSpot):
    def __init__(self, id: str, is_free: bool, vehicle: Vehicle) -> None:
        super().__init__(id, is_free, vehicle)

    def assign_vehicle(self, vehicle: Vehicle) -> None:
        pass


class Compact(ParkingSpot):
    def __init__(self, id: str, is_free: bool, vehicle: Vehicle) -> None:
        super().__init__(id, is_free, vehicle)

    def assign_vehicle(self, vehicle: Vehicle) -> None:
        pass


class Handicapped(ParkingSpot):
    def __init__(self, id: str, is_free: bool, vehicle: Vehicle) -> None:
        super().__init__(id, is_free, vehicle)

    def assign_vehicle(self, vehicle: Vehicle) -> None:
        pass
