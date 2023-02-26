from parking_lot.parking_spot import ParkingSpot, ParkingEntry
from uuid import uuid1


class ParkingTicket():
    def __init__(self, entry_time, vehicle_type, spot: ParkingSpot,
                 entry: ParkingEntry) -> None:
        self.id = self.generate_id()
        self.entry_time = entry_time
        self.vehicle_type = vehicle_type
        self.spot = spot
        self.spot = entry

    def generate_id(self):
        return uuid1()
