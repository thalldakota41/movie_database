import sqlite3


def connect():
    conn=sqlite3.connect("movies.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, director text, writer text,  year integer)")
    conn.commit()
    conn.close()

def insert(title, director, writer, year):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?,?,?,?)", (title,director,writer,year))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",director="",writer="",year=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR director=? OR writer=? OR year=?, (title,director,writer,year)")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor
    cur.execute("DELETE FROM book WHERE id=?, (id,)")
    conn.commit()
    conn.close()

def update(id,title,director,writer,year):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor
    cur.execute("UPDATE book SET title=?, director=?, writer=?, year=? WHERE id=?", (title,director,writer,year,id))
    conn.commit()
    conn.close()

connect()
