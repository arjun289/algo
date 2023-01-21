
from typing import Any, Protocol
from bs4 import BeautifulSoup
from functools import partial

"""
Client -> Adapter -> Adaptee
"""

class Config(Protocol):
    def get(self, key: str) -> Any | None:
        "Return a value associated with a key"


class XMLConfig():
    def __init__(self, bs: BeautifulSoup) -> None:
        self.bs = bs

    def get(self, key: str) -> Any | None:
        value = self.bs.find(key)
        if not value:
            return None
        return value.get_text()


class Experiment():
    def __init__(self, config: Config) -> None:
        self.config = config
        
    def load_data():
        pass

