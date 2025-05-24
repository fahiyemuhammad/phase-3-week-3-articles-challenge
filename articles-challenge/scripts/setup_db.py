from lib.db.connection import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    with open("lib/db/schema.sql") as f:
        cursor.executescript(f.read())

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Database setup complete.")