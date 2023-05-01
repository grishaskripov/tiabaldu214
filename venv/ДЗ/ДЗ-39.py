import sqlite3
def read_ava(n):
    try:
        with open(f"avatars/{n}.png", 'rb') as f:
            return f.read()

    except IOError as e:
        print(e)
        return False


with sqlite3.connect('cars.db') as con:
    con.row_factory = sqlite3.Row
cur = con.cursor()
cur.executescript("""
CREATE TABLE IF NOT EXISTS users(
name TEXT,
ava BLOB,
score INTEGER
);
""")

img = read_ava(1)
if img:
    binary = sqlite3.Binary(img)
cur.execute("INSERT INTO users VALUES('Илья', ?, 1000)", (binary,))
