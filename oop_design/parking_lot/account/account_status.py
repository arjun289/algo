from enum import Enum, auto


class AccountStats(Enum):
    ACTIVE = auto()
    CLOSED = auto()
    CANCELED = auto()
    BLACKLISTED = auto()
    NONE = auto()
