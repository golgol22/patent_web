from member.vo import db

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
   
        
# 최근 5개년 특허에서 가장 많이 등장한 단어 3개추출
class Keyword(db.Model): 
    num = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(20), nullable=False)
    keyword = db.Column(db.String(20), nullable=False)


# 분야별 특허가 가장 많은 출원인 저장
