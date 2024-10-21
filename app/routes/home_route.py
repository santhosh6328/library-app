from flask import Blueprint

home_bp = Blueprint('home', __name__)

@home_bp.route('/', methods=['GET'])
def get_books():
    return {
        "message": "Welcome to the Library App!!!",
        "github_link": "https://github.com/santhosh6328/library-app"
    }