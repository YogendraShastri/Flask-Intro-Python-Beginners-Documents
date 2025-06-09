from flask import Flask, request, jsonify
from models import db, Book
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
print("📂 Database will be created at:", os.path.abspath("db.sqlite3"))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


# create first time
with app.app_context():
    db.create_all()

# Create Book
@app.post('/book')
def create_book():
    data = request.json
    new_book = Book(title=data['title'], author=data['author'], published_year=data['published_year'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book Added Successfully', 'status_code' : 200})


# View Book
@app.get('/book')
def get_books():
    books = Book.query.all()
    return jsonify([{
        'id' : book.id,
        'Book Name' : book.title,
        'Author' : book.author,
        'Publish' : book.published_year
    } for book in books])


@app.get('/book/<book_id>')
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify({
        'Book ID': book.id,
        'Book Name' : book.title,
        'Author' : book.author,
        'Published At' : book.published_year
    })

@app.put('/book/<book_id>')
def update_book(book_id):
    data = request.json
    book = Book.query.get_or_404(book_id)
    book.title = data['title']
    book.author = data['author']
    book.published_year = data['published_year']
    db.session.commit()
    return jsonify({'message': 'Book updated'})

@app.delete('/book/<book_id>')
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': f'Book {book_id}Deleted'})



# demo run
if __name__ == "__main__":
    app.run(debug=True)
