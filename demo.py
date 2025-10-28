
from operation import *

print(add_book("001", "Python Basics", "John Doe", "Fiction", 2))
print(add_book("002", "AI 101", "Jane Smith", "Sci-Fi", 3))

print(add_member("M001", "Alice"))
print(add_member("M002", "Bob"))

print(search_book("Python"))
print(update_book("001", "Python Basics 2nd Ed", "John Doe", "Fiction"))

print(borrow_book("M001", "001"))
print(borrow_book("M001", "001"))
print(return_book("M001", "001"))

print(delete_book("002"))

