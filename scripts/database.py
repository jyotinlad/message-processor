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
                    best_before date,
                    colour text,
                    condition text,
                    weight integer
                )
            """)

        cursor.execute(
            """
                CREATE TABLE bananas (
                    id integer PRIMARY KEY,
                    best_before date,
                    colour text,
                    condition text,
                    weight integer
                )
            """)

        cursor.execute(
            """
                CREATE TABLE kiwis (
                    id integer PRIMARY KEY,
                    best_before date,
                    colour text,
                    condition text,
                    weight integer
                )
            """)

        cursor.execute(
            """
                CREATE TABLE oranges (
                    id integer PRIMARY KEY,
                    best_before date,
                    colour text,
                    condition text,
                    weight integer
                )
            """)

        cursor.execute(
            """
                CREATE TABLE pears (
                    id integer PRIMARY KEY,
                    best_before date,
                    colour text,
                    condition text,
                    weight integer
                )
            """)

        self._con.commit()

    def get_table_columns(self, table):
        cursor = self._con.cursor()
        cursor.execute(f"PRAGMA table_info({table});")

        recs = cursor.fetchall()

        return [v[1] for v in recs]

    def insert(self, table, record):
        keys = record.keys()
        valid = all(k in self.get_table_columns(table) for k in keys)
        if not valid:
            invalid = list(set(keys) - set(self.get_table_columns(table)))
            raise ValueError("invalid key(s) supplied in record: {}".format(invalid))

        insert_columns = ", ".join(keys)

        values = [record.get(k) for k in keys]
        insert_values = ", ".join("?" * len(keys))

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
