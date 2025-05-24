import sqlite3
from lib.models.article import Article

class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    @classmethod
    def all(cls):
        conn = sqlite3.connect('lib/db/database.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM magazines")
        rows = cursor.fetchall()

        conn.close()
        return [cls(id=row[0], name=row[1], category=row[2]) for row in rows]

    def articles(self):
        conn = sqlite3.connect('lib/db/database.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (self.id,))
        rows = cursor.fetchall()

        conn.close()
        return [Article(id=row[0], title=row[1], content=row[2], author_id=row[3], magazine_id=row[4]) for row in rows]

    