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