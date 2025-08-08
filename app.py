from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId


app = Flask(__name__)

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client['library_db']
books_col = db.books
borrowed_books_col = db.borrowed_books
books_collection = db['books']
borrowed_books_col = db['borrowed_books']

@app.route('/admin/books')
def admin_books():
    query = request.args.get('q', '')
    selected_category = request.args.get('category', '')

    # Fetch unique categories
    categories = books_collection.distinct('type')

    # Build filter based on query and category
    filter_query = {}
    if query:
        filter_query['$or'] = [
            {'title': {'$regex': query, '$options': 'i'}},
            {'author': {'$regex': query, '$options': 'i'}}
        ]
    if selected_category:
        filter_query['type'] = selected_category

    books = list(books_collection.find(filter_query))
    return render_template('books.html', books=books, categories=categories)

@app.route('/admin/add-book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        new_book = {
            'title': request.form['title'],
            'author': request.form['author'],
            'type': request.form['type'],
            'price': float(request.form['price']),
            'image': request.form['image']
        }
        books_collection.insert_one(new_book)
        return redirect(url_for('admin_books'))
    return render_template('add_book.html')

@app.route('/admin/edit-book/<book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    from bson.objectid import ObjectId
    book = books_collection.find_one({'_id': ObjectId(book_id)})
    if request.method == 'POST':
        updated_book = {
            'title': request.form['title'],
            'author': request.form['author'],
            'type': request.form['type'],
            'price': float(request.form['price']),
            'image': request.form['image']
        }
        books_collection.update_one({'_id': ObjectId(book_id)}, {'$set': updated_book})
        return redirect(url_for('admin_books'))
    return render_template('edit_book.html', book=book)

@app.route('/admin/delete-book/<book_id>')
def delete_book(book_id):
    from bson.objectid import ObjectId
    books_collection.delete_one({'_id': ObjectId(book_id)})
    return redirect(url_for('admin_books'))

@app.route('/admin/borrowed-books')
def borrowed_books():
    borrowed_books = list(borrowed_books_col.find())
    return render_template('borrowed_books.html', borrowed_books=borrowed_books)


@app.route("/admin/add-borrowed-book", methods=["GET", "POST"])
def add_borrowed_book():
    if request.method == "POST":
        student_name = request.form['student_name']
        student_id = request.form['student_id']
        year = request.form['year']
        book_title = request.form['book_title']
        borrow_date = request.form['borrow_date']

        borrowed_books_col.insert_one({
            "student_name": student_name,
            "student_id": student_id,
            "year": year,
            "book_title": book_title,
            "borrow_date": borrow_date
        })

        return redirect("/admin/borrowed-books")

    return render_template("add_borrowed_book.html")

@app.route("/admin/edit-borrowed-book/<id>", methods=["GET", "POST"])
def edit_borrowed_book(id):
    entry = borrowed_books_col.find_one({"_id": ObjectId(id)})

    if request.method == "POST":
        updated_entry = {
            "student_name": request.form['student_name'],
            "student_id": request.form['student_id'],
            "year": request.form['year'],
            "book_title": request.form['book_title'],
            "borrow_date": request.form['borrow_date']
        }

        borrowed_books_col.update_one({"_id": ObjectId(id)}, {"$set": updated_entry})
        return redirect("/admin/borrowed-books")

    return render_template("edit_borrowed_book.html", entry=entry)


@app.route("/admin/delete-borrowed-book/<id>")
def delete_borrowed_book(id):
    borrowed_books_col.delete_one({"_id": ObjectId(id)})
    return redirect("/admin/borrowed-books")

@app.route('/admin/categories')
def categories():
    pipeline = [
        {"$group": {"_id": "$type", "count": {"$sum": 1}}},
        {"$sort": {"_id": 1}}
    ]
    category_data = list(books_col.aggregate(pipeline))
    return render_template('categories.html', categories=category_data)

#USER PAGE ROUTES

@app.route('/user/books')
def user_books():
    query = request.args.get('q', '')
    category = request.args.get('category', '')

    filter_query = {}
    if query:
        filter_query['title'] = {'$regex': query, '$options': 'i'}
    if category:
        filter_query['type'] = category

    books = list(db.books.find(filter_query))
    categories = db.books.distinct("type")

    return render_template('user_books.html', books=books, categories=categories, query=query)


if __name__ == '__main__':
    app.run(debug=True)

