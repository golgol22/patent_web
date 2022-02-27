from member.vo import db

# 회원의 관심 분야 저장
class Field(db.Model):
    user = db.Column(db.String(50), db.ForeignKey('member.id', ondelete='CASCADE'), primary_key=True)
    field_name = db.Column(db.String(20), nullable=False)
    
class WordSearch:
    
    def __init__(self, indexNo, registerStatus, inventionTitle, ipcNumber, registerNumber, registerDate, applicationNumber, applicationDate, 
                 openNumber, openDate, publicationNumber, publicationDate, astrtCont, bigDrawing, drawing, applicantName):
        self.indexNo = indexNo # 일련번호 0
        self.registerStatus = registerStatus # 등록상태 1
        self.inventionTitle = inventionTitle # 발명의 명칭(한글) 2
        self.ipcNumber = ipcNumber # IPC 번호 3
        self.registerNumber = registerNumber # 등록번호 4
        self.registerDate = registerDate # 등록일자 5
        self.applicationNumber = applicationNumber # 출원번호 6
        self.applicationDate = applicationDate # 출원일자 7
        self.openNumber = openNumber # 공개번호 8 
        self.openDate = openDate # 공개일자 9
        self.publicationNumber = publicationNumber # 공고번호 10
        self.publicationDate = publicationDate # 공고일자 11
        self.astrtCont = astrtCont # 초록 12
        self.bigDrawing = bigDrawing # 큰 이미지 경로 13
        self.drawing = drawing # 이미지 경로 14
        self.applicantName = applicantName # 출원인 15
   
        
    def __str__(self):
        s = ''
        s += str(self.indexNo) + '|'
        s += str(self.registerStatus) + '|'
        s += str(self.inventionTitle) + '|'
        s += str(self.ipcNumber) + '|'
        s += str(self.registerNumber) + '|'
        s += str(self.registerDate) + '|'
        s += str(self.applicationNumber) + '|'
        s += str(self.applicationDate) + '|'
        s += str(self.openNumber) + '|'
        s += str(self.openDate) + '|'
        s += str(self.publicationNumber) + '|'
        s += str(self.publicationDate) + '|'
        s += str(self.astrtCont) + '|'
        s += str(self.bigDrawing) + '|'
        s += str(self.drawing) + '|'
        s += str(self.applicantName) 
        return s
