from app import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    authors = db.Column(db.String(500), nullable=False)
    average_rating = db.Column(db.Float)
    isbn = db.Column(db.String(20), nullable=False)
    isbn13 = db.Column(db.String(20))
    language_code = db.Column(db.String(10))
    num_pages = db.Column(db.Integer)
    ratings_count = db.Column(db.Integer)
    text_reviews_count = db.Column(db.Integer)
    publication_date = db.Column(db.String(50))
    publisher = db.Column(db.String(100))
    stock = db.Column(db.Integer)
    genre = db.Column(db.String(100))
    format = db.Column(db.String(50))
    dimensions = db.Column(db.String(50))
    weight = db.Column(db.String(20))
    price = db.Column(db.Float)
    edition = db.Column(db.String(50))
    synopsis = db.Column(db.Text)
    cover_image_url = db.Column(db.String(200))

    def __repr__(self):
        return f'<Book {self.title}>'

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "authors": self.authors,
            "average_rating": self.average_rating,
            "isbn": self.isbn,
            "isbn13": self.isbn13,
            "language_code": self.language_code,
            "num_pages": self.num_pages,
            "ratings_count": self.ratings_count,
            "text_reviews_count": self.text_reviews_count,
            "publication_date": self.publication_date,
            "publisher": self.publisher,
            "stock": self.stock,
            "genre": self.genre,
            "format": self.format,
            "dimensions": self.dimensions,
            "weight": self.weight,
            "price": self.price,
            "edition": self.edition,
            "synopsis": self.synopsis,
            "cover_image_url": self.cover_image_url
        }
