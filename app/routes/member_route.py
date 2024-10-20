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
   return add_members(request), 201

@members_bp.route('/members', methods=['DELETE'])
def delete_members():
    return delete_members(request), 200