# tests.py
from operation import *

assert add_book("101", "Know Python", "Vidal", "Fiction", 2) == "Book added successfully!"
assert add_member("A01", "Tom") == "Member added successfully!"
assert borrow_book("A01", "101") == "Book borrowed!"
assert return_book("A01", "101") == "Book returned!"
assert delete_book("101") == "Book deleted!"

print("All tests passed!")
