from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

class Config(object):

    SQLALCHEMY_DATABASE_URI = "mysql://root:03124223990h@127.0.0.1:3306/author_book_py04"

    SQLALCHEMY_TRACK_MODIFICATIONS = True

app.config.from_object(Config)

db = SQLAlchemy(app)


class Author(db.Model):
    __tablename__ = "tbl_authors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    books = db.relationship("Book", backref="author")

class Book(db.Model):
    __tablename__ = "tbl_books"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey("tbl_authors"))

@app.route("/")
def index():
    author_li = Author.query.all()
    return  render_template("")





if __name__ == '__main__':
    app.run(debug=True)