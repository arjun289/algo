from abc import ABC, abstractmethod
from typing import Union
from helpers.range_dict import RangeDict


class FeeModel(ABC):

    rate_model: dict[str, Union(RangeDict, int)]

    @abstractmethod
    def calculate_fee(self, ticket):
        pass


class MallFeeModel(FeeModel):
    rate_model = {
        'motorcycle': 10,
        'car': 20,
        'bus': 50
    }

    def calculate_fee(self, ticket):
        pass


class StadiumFeeModel(FeeModel):
    rate_model = {
        'motorcycle': RangeDict({
            range(0, 4): 30,
            range(4, 12): 60,
            range(12, 999999): 100
        }),
        'car': RangeDict({
            range(0, 4): 60,
            range(4, 12): 120,
            range(12, 999999): 2000
        }),
    }

    def calculate_fee(self, ticket):
        pass


class AirportFeeModel(FeeModel):
    rate_model = {
        'motorcycle': RangeDict({
            range(0, 1): 0,
            range(1, 8): 40,
            range(8, 24): 60,
            range(24, 999999): 80
        }),
        'car': RangeDict({
            range(0, 12): 60,
            range(12, 24): 80,
            range(24, 999999): 100
        }),
    }

    def calculate_fee(self, ticket):
        pass
