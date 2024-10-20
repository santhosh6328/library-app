from flask import jsonify

from app import db
from app.models.member_model import Member


def add_members(request):
    data = request.get_json()
    if not isinstance(data, list):
        return jsonify({"message": "Input should be a list of members"}), 400

    for member_data in data:
        new_member = Member(name=member_data['name'], email=member_data['email'])
        db.session.add(new_member)

    db.session.commit()
    return jsonify({"message": "Member added!"}), 201

def delete_members(request):
    data = request.get_json()
    member_ids = data.get('member_ids', [])

    members_to_delete = Member.query.filter(Member.id.in_(member_ids)).all()

    if not members_to_delete:
        return jsonify({"message": "No Members found to delete"}), 404

    for member in members_to_delete:
        db.session.delete(member)

    db.session.commit()

    return jsonify({"message": "Members deleted successfully"}), 200