"""
Concerned with storing and retrieving books from a list
"""

def add_book(name, author):
    file = open('./Utils/books.txt',"a+")
    file.write(f'{name},{author},False\n')
    file.close()

def get_all_books():
    file = open('./Utils/books.txt',"r")
    contents=file.readlines()
    file.close()
    lines=[line.strip() for line in contents]
    books = []
    name=[]
    author=[]
    read=[]
    for line in lines:
        details=line.split(",")
        name.append(details[0])
        author.append(details[1])
        read.append(details[2])
    for item in range(len(name)):
        books.append({'name':name[item],'author':author[item],'read':read[item]})
    return books

def add_book_to_file(books):
    file = open('./Utils/books.txt',"w")
    for item in books:
        file.write(f'{item["name"]},{item["author"]},{item["read"]}\n')
    file.close()


def mark_the_book_as_read(book_name):
    books=get_all_books()
    for items in books:
        if items["name"].title() == book_name.title():
            items["read"] = True
    add_book_to_file(books)

def delete_book(book_name):
    books=get_all_books()
    for items in books:
        if items["name"].title() == book_name.title():
            books.remove(items)
    add_book_to_file(books)