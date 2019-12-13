import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task text, category text, importance text, date text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM tasks")
        rows = self.cur.fetchall()
        return rows

    def insert(self, task, category, importance, date):
        self.cur.execute("INSERT INTO tasks VALUES (NULL, ?, ?, ?, ?)", (task, category, importance, date))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM tasks WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, task, category, importance, date):
        self.cur.execute("UPDATE tasks SET task=?, category=?, importance=?, date=? WHERE id=?", (task, category, importance, date, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

# db = Database('tasks.db')
# db.insert("Finish Resume", "Job Search", "High", "11/26")
