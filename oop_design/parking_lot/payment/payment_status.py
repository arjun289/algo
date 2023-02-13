from enum import Enum, auto


class PaymentStatus(Enum):
    COMPLETED = auto()
    FAILED = auto()
    PENDING = auto()
    UNPAID = auto()
    REFUNDED = auto()
