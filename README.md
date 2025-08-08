📚 Library Management System
A Flask + MongoDB based web application for managing a library.
The system has two sides:

Admin Side → Add, edit, delete books, manage borrowed books, view categories.

User Side → View all available books in the library.

🚀 Features
Admin
📖 Add, edit, and delete books

📋 View borrowed books

✏ Edit or delete borrowed book entries

🔍 Search books by title, author, or student details

🗂 Filter books by category

User
📚 View all available books

🔍 Search & filter books by category

🛠 Tech Stack
Backend: Python, Flask

Database: MongoDB

Frontend: HTML, CSS, Bootstrap

📦 Installation & Setup
1️⃣ Clone the repository
    git clone https://github.com/YOUR_USERNAME/library-management-system.git
    cd library-management-system
    
2️⃣ Install dependencies
    Make sure Python and pip are installed, then run:
      pip install -r requirements.txt
      
3️⃣ Start MongoDB
Ensure MongoDB is running locally on port 27017.
Example for Linux:
    sudo systemctl start mongod
    
4️⃣ Run the Flask app
      python app.py

5️⃣ Access in browser
    Admin Books: http://127.0.0.1:5000/admin/books
    Borrowed Books: http://127.0.0.1:5000/admin/borrowed-books
    User Books: http://127.0.0.1:5000/user/books
    
📂 Project Structure

library-management-system/
│-- app.py
│-- requirements.txt
│-- templates/
│   │-- books.html
│   │-- add_book.html
│   │-- borrowed_books.html
│   │-- add_borrowed_book.html
│   │-- edit_book.html
│   │-- edit_borrowed_book.html
│   │-- user_books.html
│   └-- categories.html
