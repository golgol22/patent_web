from member.vo import db

# 회원의 관심 분야 저장
class Field(db.Model):
    user = db.Column(db.String(50), db.ForeignKey('member.id', ondelete='CASCADE'), primary_key=True)
    field_name = db.Column(db.String(20), nullable=False)
    
class WordSearch:
    
    def __init__(self, indexNo, registerStatus, inventionTitle, ipcNumber, registerNumber, registerDate, applicationNumber, applicationDate, 
                 openNumber, openDate, publicationNumber, publicationDate, astrtCont, bigDrawing, drawing, applicantName):
        self.indexNo = indexNo
        self.registerStatus = registerStatus
        self.inventionTitle = inventionTitle
        self.ipcNumber = ipcNumber
        self.registerNumber = registerNumber
        self.registerDate = registerDate
        self.applicationNumber = applicationNumber
        self.applicationDate = applicationDate
        self.openNumber = openNumber
        self.openDate = openDate
        self.publicationNumber = publicationNumber
        self.publicationDate = publicationDate
        self.astrtCont = astrtCont
        self.bigDrawing = bigDrawing
        self.drawing = drawing
        self.applicantName = applicantName
   
        

