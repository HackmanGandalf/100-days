# import sqlite3

# db = sqlite3.connect("100-days-of-code\day 63 (2)/books-collection.db")

# cursor = db.cursor()

# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# cursor.execute("INSERT INTO books VALUES(1, 'HARRY POTTER', 'J. K. Rowlings', '9.3')")
# db.commit()


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120), unique=False, nullable=False)
    rating = db.Column(db.Float(120), unique=False, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

db.create_all()

new_book = Book(id=1, title="Harry Potter", author="J. K. Rowlings", rating="9")
db.session.add(new_book)
db.session.commit()


