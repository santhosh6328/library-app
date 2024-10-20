from datetime import datetime

from flask import jsonify

from app import db
from app.models.book_model import Book
from app.models.member_model import Member
from app.models.transaction_model import Transaction
from app.utils.utils import calculate_fee


def issue_book(request):
    data = request.get_json()
    member = Member.query.get(data['member_id'])

    if member.outstanding_debt > 500:
        return jsonify({"message": "Debt exceeds limit!"}), 400

    book = Book.query.get(data['book_id'])

    if book.stock < 1:
        return jsonify({"message": "Book out of stock!"}), 400

    transaction = Transaction(book_id=book.id, member_id=member.id, issue_date=datetime.now().timestamp())
    book.stock -= 1
    db.session.add(transaction)
    db.session.commit()

    return jsonify({"message": "Book issued!"}), 201

def return_book(request):
    data = request.get_json()
    transaction = Transaction.query.get(data['transaction_id'])

    if transaction.return_date:
        return jsonify({"message": "Book already returned!"}), 400

    transaction.return_date = datetime.now().timestamp()
    transaction.fee_charged = calculate_fee(transaction.issue_date, transaction.return_date)

    member = Member.query.get(transaction.member_id)
    member.outstanding_debt += transaction.fee_charged
    db.session.commit()

    db.session.commit()
    return jsonify({"message": "Book returned and fee charged!"}), 201