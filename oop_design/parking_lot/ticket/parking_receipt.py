from uuid import uuid1


class ParkingReceipt:
    def __init__(self, entry_time, exit_time, fees) -> None:
        self.__id = self.generate_id()
        self.entry_time = entry_time
        self.exit_time = exit_time
        self.fees = fees

    def __repr__(self) -> str:
        pass

    def generate_id(self):
        return uuid1()
