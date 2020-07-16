"""
Concerned with storing and retrieving books from a list
"""

books=[]

def add_book(name, author):
    books.append({'name':name, 'author': author, 'read': False})


def get_all_books():
     return books


def mark_the_book_as_read(book_name):
    for items in books:
        if items["name"].title() == book_name.title():
            items["read"] = True


def delete_book(book_name):
    for items in books:
        if items["name"].title() == book_name.title():
            books.remove(items)