from book import Book
import sqlite3


def cursor ():
    return sqlite3.connect('book.db').cursor()

c = cursor()
with c.connection:
    c.execute('CREATE TABLE IF NOT EXISTS books (title TEXT, pages INTEGER)')
c.connection.close()

def add_book(book):
    c = cursor()
    with c.connection:
        c.execute('INSERT INTO books VALUES (?,?)', (book.title, book.pages))
    c.connection.close()

    return c.lastrowid


def get_books():
    c = cursor()

    books = []
    
    #print(type(c.execute('SELECT * FROM books')))

    for book in c.execute('SELECT * FROM books'):
        books.append(Book(book[0], book[1]))
    c.connection.close()
     
    return books



def get_book_by_title(title):
    c = cursor()
    with c.connection:
        c.execute('SELECT * FROM books WHERE title= ?', (title,))
    data = c.fetchone()
    c.connection.close()
    
    
    if not data:
        return None
        
    return Book(data[0], data[1])


def update_book(book, new_title, new_pages):
    c = cursor()
    with c.connection:
        c.execute('UPDATE books SET title= ?, pages= ? WHERE title= ? AND pages= ?',
                (new_title, new_pages, book.title, book.pages))
    book = get_book_by_title(new_title)
    c.connection.close()

    return book


def delete_book(book):
    c = cursor()
    
    with c.connection:
        c.execute('DELETE FROM books WHERE title= ? AND pages= ?', (book.title, book.pages))
    rows = c.rowcount
    c.connection.close()

    return rows


        





    


