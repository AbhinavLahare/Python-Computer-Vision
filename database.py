import sqlite3

class EventDatabase:
    def __init__(self):
        self.conn = sqlite3.connect("events.db")
        self.create_table()

    def create_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS events (
                timestamp TEXT,
                event_type TEXT,
                value INTEGER
            )
        """)

    def insert_event(self, event):
        self.conn.execute(
            "INSERT INTO events VALUES (?, ?, ?)",
            (event["timestamp"], event["type"], event["value"])
        )
        self.conn.commit()
