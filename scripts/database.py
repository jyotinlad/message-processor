from sqlite3 import connect
from os import path


DB_FILENAME = "fruits.db"
DB_FILE = path.join("..", "storage", DB_FILENAME)


class Database:

    def __init__(self):
        # flag setup tables if database does not exist
        setup = False if path.isfile(DB_FILE) else True

        # connect to database
        self._con = connect(DB_FILE)

        # setup database
        if setup:
            self.setup()

    def setup(self):
        cursor = self._con.cursor()

        cursor.execute(
            """
                CREATE TABLE apples (
                    id integer PRIMARY KEY,
                    weight integer,
                    condition text,
                    colour text,
                    best_before date
                )
            """)

        cursor.execute(
            """
                CREATE TABLE bananas (
                    id integer PRIMARY KEY,
                    weight integer,
                    condition text,
                    colour text,
                    best_before date
                )
            """)

        cursor.execute(
            """
                CREATE TABLE kiwis (
                    id integer PRIMARY KEY,
                    weight integer,
                    condition text,
                    colour text,
                    best_before date
                )
            """)

        cursor.execute(
            """
                CREATE TABLE oranges (
                    id integer PRIMARY KEY,
                    weight integer,
                    condition text,
                    colour text,
                    best_before date
                )
            """)

        cursor.execute(
            """
                CREATE TABLE pears (
                    id integer PRIMARY KEY,
                    weight integer,
                    condition text,
                    colour text,
                    best_before date
                )
            """)

        self._con.commit()

    def get_table_columns(self, table):
        cursor = self._con.cursor()
        cursor.execute(f"PRAGMA table_info({table});")

        recs = cursor.fetchall()

        return [v[1] for v in recs]

    def insert(self, table, record):
        # columns = "weight condition colour best_before".split()
        columns = record.keys()
        valid = all(c in self.get_table_columns(table) for c in columns)
        if not valid:
            raise ValueError("invalid key(s) supplied")

        insert_columns = ", ".join(columns)

        values = [record.get(k) for k in columns]
        insert_values = ", ".join("?" * len(columns))

        cursor = self._con.cursor()
        cursor.execute(
            f"""
                INSERT INTO {table} ({insert_columns})
                VALUES({insert_values})
            """,
            values)

        self._con.commit()

    def __del__(self):
        self._con.close()


if __name__ == "__main__":
    from datetime import date
    db = Database()
    record = {
        "weight": 22,
        "condition": "good",
        "colour": "green",
        "best_before": date(2019, 1, 1)
    }
    db.insert("apples", record)

    print(db.get_table_columns("apples"))

    test = 1
