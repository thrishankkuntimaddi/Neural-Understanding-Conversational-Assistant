# memory_manager.py
import sqlite3

class MemoryManager:
    def __init__(self):
        self.conn = sqlite3.connect("memory.db")
        self.create_table()

    def create_table(self):
        query = """CREATE TABLE IF NOT EXISTS reminders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    reminder TEXT
                   )"""
        self.conn.execute(query)
        self.conn.commit()

    def store_reminder(self, reminder):
        query = "INSERT INTO reminders (reminder) VALUES (?)"
        self.conn.execute(query, (reminder,))
        self.conn.commit()

    def get_reminders(self):
        query = "SELECT * FROM reminders"
        return self.conn.execute(query).fetchall()
