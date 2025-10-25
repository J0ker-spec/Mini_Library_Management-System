# Mini_Library_Management-System
This project is a simple Library Management System built in Python.
It allows users to manage books and members using basic CRUD operations and supports borrowing and returning books.
The system is designed to be lightweight, easy to understand, and ideal for beginners learning about data structures and modular programming.

Features
•	Add, update, and delete books
•	Add and manage library members
•	Borrow and return books
•	Search for books by title or keyword
•	Validate data to avoid duplicate entries
•	Automated test script to verify functionality


How It Works
•	All data is stored in dictionaries and lists within memory (no database required).
•	operations.py defines all main functions (add, update, delete, borrow, return).
•	demo.py imports and executes these functions step-by-step to show real usage.
•	tests.py checks each function automatically to confirm correctness.

How to Run
1.	Clone the repository
2.	git clone https://github.com/yourusername/library-management-system.git
3.	cd library-management-system
4.	Run the demo
5.	python demo.py
6.	Run the tests
7.	python tests.py
You should see messages confirming that each function works correctly.

Example Output
Book added successfully.
Member added successfully.
Book borrowed!
Book returned!
Book deleted!
All tests passed!

Technologies Used
•	Python 
•	No external libraries required (fully built with core Python)

Future Improvements
•	Add file or database storage
•	Add graphical user interface (GUI)
•	Track borrowed book history per member
•	Add login system for admin and users

Author
Vidal Olu-Jones
Student, Limkokwing University of Creative Technology – Sierra Leone

