from flask import session
import requests
from bs4 import BeautifulSoup
from member.vo import db
from patent_search.vo import WordSearch, Keyword, Field
from konlpy.tag import Okt
from collections import Counter

class DBService: # field 테이블에 저장, 검색
    def add(self, f_name):
        user = session['login_id']
        f = Field(user=user, field_name=f_name)
        db.session.add(f)
        db.session.commit()
    
    def getById(self):
        res = []
        user = session['login_id']
        return Field.query.get(user)
    
    def edit(self, f_name):
        user = session['login_id']
        f = self.getById()
        f.field_name = f_name
        db.session.commit()
        
class Service: # Keyword테이블에 년도별 빈도수가 많은 값 DB에 저장
    def add(self, yk:Keyword):
        db.session.add(yk)
        db.session.commit()
    
    def getByAll(self, year):
        return Keyword.query.filter(Keyword.year==year).all()
    
class SearchService:
    def __init__(self):
        self.key = 'ooRP9Oq6WkfYDhiOcE/YjBxb91I5spT1hpEJPl01lMQ='

    # 일반 검색
    def getWordSearch(self, word=None, year=-1, patent=None, utility=None, numOfRows=0, pageNo=0):
        url = 'http://plus.kipris.or.kr/kipo-api/kipi/patUtiModInfoSearchSevice/getWordSearch?'
        
        if word != None:
            url += '&word=' + word
        
        if year != -1:
            url += '&year=' + str(year)
            
        if patent != None:
            url += '&patent=' + patent
            
        if utility != None:
            url += '&utility=' + utility
            
        if numOfRows != 0:
            url += '&numOfRows=' + str(numOfRows)
            
        if pageNo != 0:
            url += '&pageNo=' + str(pageNo)
            
        url += '&ServiceKey=' + self.key
        html = requests.get(url).text 
        root = BeautifulSoup(html, 'lxml-xml') 
        print(root)
        resultCode = root.find('resultCode').text
        if resultCode != '00':  
            msg = root.find('resultMag').text
            print(msg)
            return 
    
        items = root.find_all('item') 
        numOfRows = root.find('numOfRows').text
        pageNo = root.find('pageNo').text
        totalCount = root.find('totalCount').text 
        res = []
        
        for item in items:
            indexNo = item.find('indexNo').text
            registerStatus = item.find('registerStatus').text
            inventionTitle = item.find('inventionTitle').text
            ipcNumber =  item.find('ipcNumber').text
            registerNumber = item.find('registerNumber').text
            registerDate = item.find('registerDate').text
            applicationNumber = item.find('applicationNumber').text
            applicationDate = item.find('applicationDate').text
            openNumber = item.find('openNumber').text
            openDate = item.find('openDate').text
            publicationNumber = item.find('publicationNumber').text
            publicationDate = item.find('publicationDate').text
            astrtCont = item.find('astrtCont').text
            bigDrawing = item.find('bigDrawing').text
            drawing = item.find('drawing').text
            applicantName = item.find('applicantName').text
            
            res.append(WordSearch(indexNo=indexNo, registerStatus=registerStatus, inventionTitle=inventionTitle, ipcNumber=ipcNumber,
                    registerNumber=registerNumber, registerDate=registerDate, applicationNumber=applicationNumber, applicationDate=applicationDate, 
                    openNumber=openNumber, openDate=openDate, publicationNumber=publicationNumber, publicationDate=publicationDate, astrtCont=astrtCont,
                    bigDrawing=bigDrawing, drawing=drawing, applicantName=applicantName))

        return res, numOfRows, pageNo, totalCount

    # 항목별 검색 (전체 검색) 
    def getAdvancedSearch(self, inventionTitle=None, astrtCont=None, claimScope=None, ipcNumber=None, applicationNumber=None, openNumber=None, publicationNumber=None, registerNumber=None, 
                          priorityApplicationNumber=None, internationalApplicationNumber=None, internationOpenNumber=None, applicationDate=None, openDate=None, publicationDate=None, registerDate=None, 
                          priorityApplicationDate=None, internationalApplicationDate=None, applicant=None, inventors=None, agent=None, rightHoler=None, patent=None, utility=None, lastvalue=None, numOfRows=0, 
                          pageNo=0, sortSpec=None, descSort=None):
        url = 'http://plus.kipris.or.kr/kipo-api/kipi/patUtiModInfoSearchSevice/getAdvancedSearch?'
        
        
        if inventionTitle != None:
            url += '&inventionTitle=' + inventionTitle
        
        if astrtCont != None:
            url += '&astrtCont=' + astrtCont
            
        if claimScope != None:
            url += '&claimScope=' + claimScope	
            
        if ipcNumber != None:
            url += '&ipcNumber=' + ipcNumber	
            
        if applicationNumber != None:
            url += '&applicationNumber=' + applicationNumber	
            
        if publicationNumber != None:
            url += '&publicationNumber=' + publicationNumber	
            
        if registerNumber != None:
            url += '&registerNumber=' + registerNumber		
            
        if priorityApplicationNumber != None:
            url += '&priorityApplicationNumber=' + priorityApplicationNumber		
            
        if internationalApplicationNumber != None:
            url += '&internationalApplicationNumber=' + internationalApplicationNumber
            
        if internationOpenNumber != None:
            url += '&internationOpenNumber=' + internationOpenNumber
            
        if applicationDate != None:
            url += '&applicationDate=' + applicationDate
            
        if openDate != None:
            url += '&openDate=' + openDate	
            
        if publicationDate != None:
            url += '&publicationDate=' + publicationDate
            
        if registerDate != None:
            url += '&registerDate=' + registerDate	
            
        if priorityApplicationDate != None:
            url += '&priorityApplicationDate=' + priorityApplicationDate	
            
        if internationalApplicationDate != None:
            url += '&internationalApplicationDate=' + internationalApplicationDate
            
        if applicant != None:
            url += '&applicant=' + applicant
            
        if inventors != None:
            url += '&inventors=' + inventors	
            
        if agent != None:
            url += '&agent=' + agent	
            
        if rightHoler != None:
            url += '&rightHoler=' + rightHoler	
            
        if patent != None:
            url += '&patent=' + patent	
            
        if utility != None:
            url += '&utility=' + utility	
            
        if lastvalue != None:
            url += '&lastvalue=' + lastvalue
            
        if numOfRows != 0:
            url += '&numOfRows=' + str(numOfRows)		
            
        if pageNo != 0:
            url += '&pageNo=' + str(pageNo)		
            
        if sortSpec != None:
            url += '&sortSpec=' + sortSpec		
            
        if descSort != None:
            url += '&descSort=' + descSort		
            
        url += '&ServiceKey=' + self.key	
        
        html = requests.get(url).text 
        root = BeautifulSoup(html, 'lxml-xml') 
        resultCode = root.find('resultCode').text
        if resultCode != '00':  
            msg = root.find('resultMag').text
            print(msg)
            return 
    
        item = root.find_all('item') 
        numOfRows = root.find('numOfRows').text
        pageNo = root.find('pageNo').text
        totalCount = root.find('totalCount').text 
        res = []

        for i in item:
            indexNo = i.find('indexNo').text
            registerStatus = i.find('registerStatus').text
            inventionTitle = i.find('inventionTitle').text
            ipcNumber =  i.find('ipcNumber').text
            registerNumber = i.find('registerNumber').text
            registerDate = i.find('registerDate').text
            applicationNumber = i.find('applicationNumber').text
            applicationDate = i.find('applicationDate').text
            openNumber = i.find('openNumber').text
            openDate = i.find('openDate').text
            publicationNumber = i.find('publicationNumber').text
            publicationDate = i.find('publicationDate').text
            astrtCont = i.find('astrtCont').text
            bigDrawing = i.find('bigDrawing').text
            drawing = i.find('drawing').text
            applicantName = i.find('applicantName').text
            
            res.append(WordSearch(indexNo=indexNo, registerStatus=registerStatus, inventionTitle=inventionTitle, ipcNumber=ipcNumber,
                    registerNumber=registerNumber, registerDate=registerDate, applicationNumber=applicationNumber, applicationDate=applicationDate, 
                    openNumber=openNumber, openDate=openDate, publicationNumber=publicationNumber, publicationDate=publicationDate, astrtCont=astrtCont,
                    bigDrawing=bigDrawing, drawing=drawing, applicantName=applicantName))
            
        return res, numOfRows, pageNo, totalCount
        
    # 년도별(최근 5개년) 데이터 추출해서 빈도수가 높은 단어 반환
    def getYearKeywordSearch(self, year):
        res = []
        inventionTitle = '' 
        term = str(year) + '0101~' + str(year) + '1231'
        for pageNo in range(1, 6):
            res, numOfRows, pageNo, totalCounts = self.getAdvancedSearch(applicationDate=term, pageNo= pageNo, numOfRows=500)
        
            print(str(year) + '년 총 개수: ' + str(totalCounts))
            print(str(year) + '년 불러온 행의 개수: ' + str(len(res)))
        
            for r in res:
                inventionTitle +=  ' / ' + str(r.inventionTitle)
            
        okt = Okt()
        sentence_tag = []
        sentence_tag = okt.pos(inventionTitle)
        words = ['시스템', '서비스', '정보', '제공', '기초', '기반', '관리',  '표시', '연결', 
                 '형성', '기능', '구조', '장치', '구비', '이용', '방지', '조절', '제조', '보조', 
                 '포함', '모듈', '용기', '방법', '제어', '기구', '사용', '기용', '조성', '이의', '조립', '처리']

        noun_adj_list = []
        for word, tag in sentence_tag:
            if tag in ['Noun'] and len(word) != 1 and word not in words: 
                noun_adj_list.append(word)

        counts = Counter(noun_adj_list)
        tags = counts.most_common(10)
        return tags
        
    
 


