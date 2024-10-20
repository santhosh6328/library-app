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

@members_bp.route('/members', methods=['DELETE'])
def delete_members():
    data = request.get_json()
    member_ids = data.get('member_ids', [])

    members_to_delete = Member.query.filter(Member.id.in_(member_ids)).all()

    if not members_to_delete:
        return jsonify({"message": "No Members found to delete"}), 404

    for member in members_to_delete:
        db.session.delete(member)

    db.session.commit()

    return jsonify({"message": "Members deleted successfully"}), 200