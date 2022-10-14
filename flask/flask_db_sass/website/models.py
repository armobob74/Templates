from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TestModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String)


