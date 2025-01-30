import json

book = {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925,
    "ISBN": 9780743273565
}

with open("book.json", "w") as file:
    json.dump(book, file)

with open("book.json", "r") as file:
    book_info = json.load(file)


print(f"""
    Book Information:
    Title: {book_info["title"]}
    Author: {book_info["author"]}
    Year: {book_info["year"]}
    ISBN: {book_info["ISBN"]}
    """)