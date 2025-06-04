import sqlite3
from lib.db.get_connection import get_connection  

class Author:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (self.name,))
        self.id = cursor.lastrowid
        conn.commit()
        conn.close()

    @classmethod
    def all(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors")
        rows = cursor.fetchall()
        conn.close()
        return [cls(id=row[0], name=row[1]) for row in rows]

    @classmethod
    def find_by_name(cls, name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE name = ?", (name,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(id=row[0], name=row[1])
        return None

    def articles(self):
        from lib.models.article import Article
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id = ?", (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [Article(id=row[0], title=row[1], content=row[4], author_id=row[2], magazine_id=row[3]) for row in rows]

    def magazines(self):
        from lib.models.magazine import Magazine
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT magazines.*
            FROM magazines
            JOIN articles ON articles.magazine_id = magazines.id
            WHERE articles.author_id = ?
        """, (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [Magazine(id=row[0], name=row[1], category=row[2]) for row in rows]

    def add_article(self, title, content, magazine):
        from lib.models.article import Article
        article = Article(title=title, content=content, author_id=self.id, magazine_id=magazine.id)
        article.save()
        return article

    @classmethod
    def top_author(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT authors.*, COUNT(articles.id) AS article_count
            FROM authors
            JOIN articles ON authors.id = articles.author_id
            GROUP BY authors.id
            ORDER BY article_count DESC
            LIMIT 1
        """)
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(id=row[0], name=row[1])
        return None