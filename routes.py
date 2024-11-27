from flask import Blueprint, request, jsonify
from models import db, User, Book, Category, Progress

api = Blueprint('api', __name__)

@api.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return jsonify(user_id=user.user_id), 201

@api.route('/books', methods=['POST'])
def create_book():
    data = request.json
    book = Book(**data)
    db.session.add(book)
    db.session.commit()
    return jsonify(book_id=book.book_id), 201

@api.route('/categories', methods=['POST'])
def create_category():
    data = request.json
    category = Category(**data)
    db.session.add(category)
    db.session.commit()
    return jsonify(category_id=category.category_id), 201

@api.route('/progress', methods=['POST'])
def create_progress():
    data = request.json
    progress = Progress(**data)
    db.session.add(progress)
    db.session.commit()
    return jsonify(progress_id=progress.progress_id), 201