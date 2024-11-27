from database import db

class User(db.Model):
    user_id = db.Column(db.String, primary_key=True)
    user_uuid = db.Column(db.String)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    role = db.Column(db.String)
    date_of_birth = db.Column(db.Date)
    deleted_at = db.Column(db.Date)
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)

class Book(db.Model):
    book_id = db.Column(db.String, primary_key=True)
    book_uuid = db.Column(db.String)
    title = db.Column(db.String)
    author = db.Column(db.String)
    genre = db.Column(db.String)
    publication_date = db.Column(db.Date)
    ISBN = db.Column(db.String)
    language = db.Column(db.String)
    summary = db.Column(db.Text)
    cover_image_url = db.Column(db.String)
    source_url = db.Column(db.String)
    deleted_at = db.Column(db.Date)
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)

class Category(db.Model):
    category_id = db.Column(db.String, primary_key=True)
    category_uuid = db.Column(db.String)
    name = db.Column(db.String)
    description = db.Column(db.Text)
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)

class Progress(db.Model):
    progress_id = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('user.user_id'))
    book_id = db.Column(db.String, db.ForeignKey('book.book_id'))
    chapter_id = db.Column(db.String)
    progress_percentage = db.Column(db.Numeric)
    last_read_at = db.Column(db.Date)
    deleted_at = db.Column(db.Date)
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)