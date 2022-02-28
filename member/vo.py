from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

class Member(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    pwd = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    tel = db.Column(db.String(50), nullable=False)
    
class MyCal(db.Model):
    user = db.Column(db.String(50), db.ForeignKey('member.id', ondelete='CASCADE'), primary_key=True)
    date = db.Column(db.String(20), nullable=False)