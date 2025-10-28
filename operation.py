
books = {}
members = []
genres = ["Fiction", "Non-Fiction", "Sci-Fi"]

def add_book(isbn, title, author, genre, total_copies):
    if isbn not in books:
        if genre in genres:
            books[isbn] = {"title": title, "author": author, "genre": genre, "total_copies": total_copies}
            return "Book added successfully!"
        else:
            return "Invalid genre!"
    else:
        return "Book already exists!"

def add_member(id, name):
    existing_ids = [m["id"] for m in members]
    if id not in existing_ids:
        members.append({"id": id, "name": name, "borrowed_books": []})
        return "Member added successfully!"
    else:
        return "Member already exists!"


def search_book(keyword):
    # Instead of loops, we’ll use a small trick with list comprehension
    result = next((b for b in books.values() if keyword in b["title"] or keyword in b["author"]), None)
    if result:
        return result
    return "Book not found!"
def update_book(isbn, new_title, new_author, new_genre):
    if isbn in books:
        books[isbn]["title"] = new_title
        books[isbn]["author"] = new_author
        books[isbn]["genre"] = new_genre
        return "Book updated!"
    return "Book not found!"


def delete_book(isbn):
    if isbn in books:
        del books[isbn]
        return "Book deleted!"
    return "Book not found!"


def borrow_book(member_id, isbn):
    member = next((m for m in members if m["id"] == member_id), None)
    if not member:
        return "Member not found!"
    if isbn not in books:
        return "Book not found!"
    if len(member["borrowed_books"]) >= 3:
        return "Borrow limit reached!"
    if books[isbn]["total_copies"] <= 0:
        return "No copies left!"

    member["borrowed_books"].append(isbn)
    books[isbn]["total_copies"] -= 1
    return "Book borrowed!"


def return_book(member_id, isbn):
    member = next((m for m in members if m["id"] == member_id), None)
    if not member:
        return "Member not found!"
    if isbn not in member["borrowed_books"]:
        return "This book was not borrowed!"

    member["borrowed_books"].remove(isbn)
    books[isbn]["total_copies"] += 1
    return "Book returned!"

