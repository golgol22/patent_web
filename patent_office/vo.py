class Office:
    def __init__(self, office_name, office_apply, office_referee, office_score):
        self.office_name = office_name
        self.office_apply = office_apply
        self.office_referee = office_referee
        self.office_score = office_score
        
    def __str__(self):
        s = ''
        s += '사무소 이름: '+self.office_name + '\n'
        s += '출원: ' + self.office_apply + '\n'
        s += '심판: ' + self.office_referee + '\n'
        s += '평점: ' + self.office_score 
        return s