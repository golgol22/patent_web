from member.vo import db

class OfficeDB(db.Model):
    num = db.Column(db.Integer, primary_key=True)  
    user = db.Column(db.String(50), db.ForeignKey('member.id', ondelete='CASCADE'))
    office_name = db.Column(db.String(30), nullable=False)
    office_apply = db.Column(db.String(30), nullable=False)
    office_referee = db.Column(db.String(30), nullable=False)
    office_score = db.Column(db.String(30), nullable=False)

class Office:
    def __init__(self, office_name, office_apply, office_referee, office_score):
        self.office_name = office_name
        self.office_apply = office_apply
        self.office_referee = office_referee
        self.office_score = office_score
        
    def __str__(self):
        s = ''
        s += self.office_name + '|'
        s += self.office_apply + '|'
        s += self.office_referee + '|'
        s += self.office_score 
        return s
    
