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
    return issue_book(request), 201


@transactions_bp.route('/return_book', methods=['POST'])
def return_book():
    return return_book(request), 201


@transactions_bp.route('/all_transactions', methods=['GET'])
def all_transactions():
    transactions = Transaction.query.all()
    return jsonify([transaction.to_dict() for transaction in transactions])
