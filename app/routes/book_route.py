from flask import Blueprint, request, jsonify
from app.models.book_model import Book
from app import db

books_bp = Blueprint('books', __name__)

@books_bp.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

@books_bp.route('/books', methods =['POST'])
def add_books():
    return add_books(request), 201

@books_bp.route('/books', methods=['DELETE'])
def delete_books():
    return delete_books(request), 200

@books_bp.route('/books/search', methods=['GET'])
def search_books():
    return search_books(request), 200