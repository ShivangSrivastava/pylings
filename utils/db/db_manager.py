import sqlite3

from utils.constants import DB_PATH


class DBManager:
    def __init__(self) -> None:
        self.conn = sqlite3.connect(DB_PATH)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
