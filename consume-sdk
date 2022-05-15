import tkinter
from tkinter import END
from book import Book
import bookSDK


def add_to_list():

    book = Book(title_entry.get(), pages_entry.get())
    
    if (bookSDK.add_book(book)): 
        listbox.insert(END, book)
        title_entry.delete(0,END)
        pages_entry.delete(0,END)

def remove_from_list():
    listbox.delete(listbox.curselection())



tk = tkinter.Tk()
tk.title('Testing a listbox')


listbox = tkinter.Listbox(tk)
listbox.pack()

title = tkinter.Label(tk, text= "Book title:")
title.pack()

title_entry = tkinter.Entry(tk)
title_entry.pack()

pages = tkinter.Label(tk, text= "Book pages:")
pages.pack()

pages_entry = tkinter.Entry(tk)
pages_entry.pack()


button = tkinter.Button(tk, text= 'Add Book', command=add_to_list)
button.pack()

button = tkinter.Button(tk, text= 'Remove Selected Book', command=remove_from_list)
button.pack()

tk.mainloop()







# low = 0
# high = 20

# rand = randint(low, high)
# print(rand)

# def check(guess):
#   if guess < rand:
#     tkinter.Label(tk, text= f'{guess} is too low').pack()
#   elif guess > rand:
#     tkinter.Label(tk, text= f'{guess} is too high').pack()
#   else:
#     messagebox.showinfo('you win', f'{guess} is correct')



# tk = tkinter.Tk()

# tk.title('Guessing game')

# label = tkinter.Label(tk, text= f'Guess a number from {low} to {high}')
# label.pack()


# entry = tkinter.Entry(tk)
# entry.pack()




# button = tkinter.Button(tk, text= 'Guess', command=lambda: check(int(entry.get())))
# button.pack()



# tk.mainloop()















#CONSOLE APP QUE LLAMA A consume-sdk.py

# import bookSDK
# from book import Book

# def print_menu():
#     print('''Choose an option:
#     1. Print all books
#     2. Add a book
#     3. Update a book
#     4. Delete a book 
#     5. Get a book by title
#     ''')

# while True:
#     print_menu()
#     response = int (input())
#     if response == 1:
#         for book in bookSDK.get_books():
#             print(book)
#     elif response == 2:
#         print('What is the name of the book?: ')
#         title = input()
#         print('How many pages is the book?: ')
#         pages = int(input())
#         book = Book(title, pages)
#         bookSDK.add_book(book)
#     elif response == 3:
#         print('Current title: ')
#         title = input()
#         print('Current number of pages: ')
#         pages = input()

#         book = Book(title, pages)

#         print('New title: ')
#         new_title = input()
#         print('New number of pages: ')
#         new_pages = input()

#         print(bookSDK.update_book(book, new_title, new_pages))

#     elif response == 4:
#         print('Book Title: ')
#         title = input()
#         print('Book number of pages: ')
#         pages = input()
#         print (bookSDK.delete_book(Book(title, pages)))
#     elif response == 5:
#         print('Title: ')
#         title = input()
#         print (bookSDK.get_book_by_title(title))
#     else:
#         print('Thanks for using my app')
#         break



























