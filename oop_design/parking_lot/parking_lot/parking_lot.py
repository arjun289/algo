from payment.fee_model import FeeModel
from uuid import uuid1


class ParkingLot:
    def __init__(self, fee_model: FeeModel, address) -> None:
        self.fee_model = fee_model
        self.address = address


class ParkingEntry:
    def __init__(self, name: str, parking_lot: ParkingLot) -> None:
        self.id = uuid1()
        self.name = name
        self.parking_lot = parking_lot

    def generate_uuid(self):
        return uuid1()


class ParkingExit:
    def __init__(self, name: str, parking_lot: ParkingLot) -> None:
        self.id = uuid1()
        self.name = name

    def generate_uuid(self):
        return uuid1()
