from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

class Member(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    pwd = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    tel = db.Column(db.String(50), nullable=False)
    
    # def __init__(self, id:str=0, pwd:str=None, name:str=None, email:str=None, tel:str=None):
    #     self.id = id
    #     self.pwd = pwd
    #     self.name = name
    #     self.email = email
    #     self.tel = tel
        
    # def __str__(self): 
    #     return 'id :' + self.id + ' / pwd :' + self.pwd + ' / name : ' + self.name + ' / email :' + self.email + '/ tel : ' + self.tel