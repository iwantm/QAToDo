from application import db


class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    completed = db.Column(db.Boolean, default=False)
