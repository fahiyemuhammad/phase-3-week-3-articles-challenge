import sqlite3

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    @classmethod
    def all(cls):
        conn = sqlite3.connect('lib/db/database.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM articles")
        rows = cursor.fetchall()

        conn.close()
        return [cls(id=row[0], title=row[1], content=row[2], author_id=row[3], magazine_id=row[4]) for row in rows]

    def author(self):
        from lib.models.author import Author
        conn = sqlite3.connect('lib/db/database.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM authors WHERE id = ?", (self.author_id,))
        row = cursor.fetchone()

        conn.close()
        return Author(id=row[0], name=row[1]) if row else None

    def magazine(self):
        from lib.models.magazine import Magazine
        conn = sqlite3.connect('lib/db/database.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM magazines WHERE id = ?", (self.magazine_id,))
        row = cursor.fetchone()

        conn.close()
        return Magazine(id=row[0], name=row[1], category=row[2]) if row else None