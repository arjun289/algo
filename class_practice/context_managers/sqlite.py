import sqlite3
import logging

class SQLite:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.connecton = sqlite3.connect(self.file_name)

    def __enter__(self):
        logging.info("Calling __enter__")        
        return self.connecton.cursor()

    def __exit__(self, exc_type, exc_value, traceback):
        logging.info("Calling __exit__")
        self.connecton.commit()
        self.connecton.close()


from contextlib import contextmanager

@contextmanager
def open_db(file_name: str):
    connection = sqlite3.connect(file_name)
    try:
        cursor = connection.cursor()
    finally:
        connection.commit()
        connection.close()
