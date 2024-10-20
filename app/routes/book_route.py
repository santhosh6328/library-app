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
    data = request.get_json()
    new_book = Book(
        title=data['title'],
        authors=data['authors'],
        average_rating=data.get('average_rating', None),
        isbn=data['isbn'],
        isbn13=data.get('isbn13', None),
        language_code=data.get('language_code', None),
        num_pages=data.get('num_pages', None),
        ratings_count=data.get('ratings_count', None),
        text_reviews_count=data.get('text_reviews_count', None),
        publication_date=data.get('publication_date', None),
        publisher=data.get('publisher', None),
        stock=data['stock'],
        genre=data.get('genre', None),
        format=data.get('format', None),
        dimensions=data.get('dimensions', None),
        weight=data.get('weight', None),
        price=data.get('price', None),
        edition=data.get('edition', None),
        synopsis=data.get('synopsis', None),
        cover_image_url=data.get('cover_image_url', None)
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"message": "Book added!"}), 201

@books_bp.route('/books/delete', methods=['DELETE'])
def delete_books():
    data = request.get_json()
    book_ids = data.get('book_ids', [])

    books_to_delete = Book.query.filter(Book.id.in_(book_ids)).all()

    if not books_to_delete:
        return jsonify({"message": "No books found to delete"}), 404

    for book in books_to_delete:
        db.session.delete(book)

    db.session.commit()

    return jsonify({"message": "Books deleted successfully"}), 200

@books_bp.route('/books/search', methods=['GET'])
def search_books():
    # Get the query parameters
    title = request.args.get('title', None)
    author = request.args.get('author', None)

    query = Book.query

    if title:
        query = query.filter(Book.title.ilike(f"%{title}%"))  # Search books by title (case-insensitive)
    if author:
        query = query.filter(Book.authors.ilike(f"%{author}%"))  # Search books by author (case-insensitive)

    books = query.all()

    if not books:
        return jsonify({"message": "No books found matching the criteria"}), 404

    return jsonify([book.to_dict() for book in books]), 200
