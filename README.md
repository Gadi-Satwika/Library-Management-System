# 📚 Library Management System

This project is a simple **Library Management System** that includes:

- ✅ User Signup/Login
- ✅ Admin Login/Signup
- ✅ CRUD Operation OnBooks
- ✅ User Details(Borrowed/Returned)
- ✅ Support Tickets
- ✅ LogOut

  Technolgies Used:
- ✅ Frontend: HTML, CSS, Bootstrap, JavaScript
- ✅ Backend: Python (Flask)
- ✅ Database: MongoDB

---

## ✨ Features

### 👤 User
- Sign up with **Name**, **Email**, **Mobile Number**, and **Password**
- Login using email and password
- View library dashboard (future scope: borrow books, view history, etc.)

### 🛠️ Admin
- Secure login with admin credentials
- Manage books, users, and track activity (to be implemented)

---

## 🗂️ Project Structure

library-management/
public/
│
├── static/
│ ├── css/
│ │ └── styles.css
│ └── js/
│ └── scripts.js
│
├── templates/
│ ├── user_signup.html
│ ├── user_login.html
│ ├── user_dashboard.html
│ ├── admin_signup.html
│ ├── admin_login.html
│ ├── admin_dashboard.html
│ ├── forgot_password.html
│ ├── reset_password.html
│
├── app.py
├── requirements.txt
└── README.md


#Satwika

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


🎫 Support Ticket System

The project now includes a Support Ticket feature that allows users to raise issues or requests directly within the system.

🔹 Features

Users can create new support tickets with details (title, description, priority).

Tickets are stored in the database for tracking.

Admins can view, update status, and respond to tickets.

Status options: Open, In Progress, Resolved, Closed.

Users can track the progress of their tickets from their dashboard.

Live Preview: https://library-management-system-fxus.onrender.com

~ Follow For More
~ Any Problem? Drop a mail-> satwikagadi2005@gmail.com

#ThankYou


