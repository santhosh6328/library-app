from flask import jsonify

from app import db
from app.models.book_model import Book


def add_books(request):
    data = request.get_json()

    if not isinstance(data, list):
        return jsonify({"message": "Input should be a list of books"}), 400

    for book_data in data:
        new_book = Book(
            title=book_data['title'],
            authors=book_data['authors'],
            average_rating=book_data.get('average_rating', None),
            isbn=book_data['isbn'],
            isbn13=book_data.get('isbn13', None),
            language_code=book_data.get('language_code', None),
            num_pages=book_data.get('num_pages', None),
            ratings_count=book_data.get('ratings_count', None),
            text_reviews_count=book_data.get('text_reviews_count', None),
            publication_date=book_data.get('publication_date', None),
            publisher=book_data.get('publisher', None),
            stock=book_data['stock'],
            genre=book_data.get('genre', None),
            format=book_data.get('format', None),
            dimensions=book_data.get('dimensions', None),
            weight=book_data.get('weight', None),
            price=book_data.get('price', None),
            edition=book_data.get('edition', None),
            synopsis=book_data.get('synopsis', None),
            cover_image_url=book_data.get('cover_image_url', None)
        )
        db.session.add(new_book)

    db.session.commit()
    return jsonify({"message": "Book added!"}), 201

def delete_books(request):
    data = request.get_json()
    book_ids = data.get('book_ids', [])

    books_to_delete = Book.query.filter(Book.id.in_(book_ids)).all()

    if not books_to_delete:
        return jsonify({"message": "No books found to delete"}), 404

    for book in books_to_delete:
        db.session.delete(book)

    db.session.commit()

    return jsonify({"message": "Books deleted successfully"}), 200

def search_books(request):
    # Get the query parameters
    title = request.args.get('title', None)
    author = request.args.get('author', None)

    query = Book.query

    if title:
        query = query.filter(Book.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(Book.authors.ilike(f"%{author}%"))

    books = query.all()

    if not books:
        return jsonify({"message": "No books found matching the criteria"}), 404

    return jsonify([book.to_dict() for book in books]), 200