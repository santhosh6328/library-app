from flask import Blueprint, request, jsonify
from .models import Book
from . import db

main = Blueprint('main', __name__)


@main.route('/books', methods=['GET', 'POST'])
def manage_books():
    if request.method == 'POST':
        data = request.get_json()
        new_book = Book(title=data['title'], author=data['author'], stock=data['stock'])
        db.session.add(new_book)
        db.session.commit()
        return jsonify({"message": "Book added!"}), 201
    else:
        books = Book.query.all()
        return jsonify([book.title for book in books])

