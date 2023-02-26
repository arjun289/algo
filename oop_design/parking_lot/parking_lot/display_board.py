class DisplayBoard:
    def __init__(self, id, handicapped_spot, compact_spot, large_spot,
                 motorcycle_spot) -> None:
        self._id = id
        self.__handicapped_spot = handicapped_spot
        self.__compact_spot = compact_spot
        self.__large_spot = large_spot
        self.__motorcycle_spot = motorcycle_spot

    def show_free_slots(self):
        pass
