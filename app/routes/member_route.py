from flask import Blueprint, request, jsonify
from app.models.member_model import Member
from app import db

members_bp = Blueprint('members', __name__)

@members_bp.route('/members', methods=['GET'])
def get_members():
   members = Member.query.all()
   return jsonify([member.to_dict() for member in members])

@members_bp.route('/members', methods=['POST'])
def add_members():
   data = request.get_json()
   new_member = Member(name=data['name'], email=data['email'])
   db.session.add(new_member)
   db.session.commit()
   return jsonify({"message": "Member added!"}), 201