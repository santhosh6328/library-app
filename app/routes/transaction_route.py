from datetime import date, datetime

from flask import Blueprint, request, jsonify
from app.models.book_model import Book
from app.models.member_model import Member
from app.models.transaction_model import Transaction
from app import db
from app.utils.utils import calculate_fee

transactions_bp = Blueprint('transaction', __name__)


@transactions_bp.route('/issue_book', methods=['POST'])
def issue_book():
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


@transactions_bp.route('/return_book', methods=['POST'])
def return_book():
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


@transactions_bp.route('/all_transactions', methods=['GET'])
def all_transactions():
    transactions = Transaction.query.all()
    return jsonify([transaction.to_dict() for transaction in transactions])
