"""
Concerned with storing and retrieving books from a list
"""

books=[
]

def add_book(name, author):
    books.append({'name':name, 'author': author, 'read': False})

def list_books():
     for items in books:
        print(f'\nThe book "{items["name"]}" was written by {items["author"]} and the status of read is {items["read"]}.')

def prompt_read_book():
    book_name = input("Enter the book name read : ")
    for items in books:
        if items["name"].title() == book_name.title():
            items["read"] = True

def prompt_delete_book():
    book_name = input("Enter the book name needs to be deleted : ")
    for items in books:
        if items["name"].title() == book_name.title():
            books.remove(items)