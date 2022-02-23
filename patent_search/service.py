import requests
from bs4 import BeautifulSoup
from vo import WordSearch

class Service:
    def __init__(self):
        self.key = 'ooRP9Oq6WkfYDhiOcE/YjBxb91I5spT1hpEJPl01lMQ='

    # 일반 검색
    def getWordSearch(self, word, year):
        url = 'http://plus.kipris.or.kr/kipo-api/kipi/patUtiModInfoSearchSevice/getWordSearch?'
        url += 'word=' + word
        url += 'year=' + year
        url += '&ServiceKey=' + self.key
        html = requests.get(url).text 
        root = BeautifulSoup(html, 'lxml-xml') 
        print(root)
        resultCode = root.find('resultCode').text
        if resultCode != '00':  
            msg = root.find('resultMag').text
            print(msg)
            return 
    
        items = root.find_all('items') 
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

        return res

    # 항목별 검색 (전체 검색)
    def getAdvancedSearch(self, inventionTitle, astrtCont, claimScope, ipcNumber, applicationNumber, openNumber, publicationNumber, registerNumber, 
                          priorityApplicationNumber, internationalApplicationNumber, internationOpenNumber, applicationDate, openDate, publicationDate, registerDate, 
                          priorityApplicationDate, internationalApplicationDate, applicant, inventors, agent, rightHoler, patent, utility, lastvalue, numOfRows, 
                          pageNo, sortSpec, descSort):
        url = 'http://plus.kipris.or.kr/kipo-api/kipi/patUtiModInfoSearchSevice/getAdvancedSearch?'
        url += 'inventionTitle=' + inventionTitle
        url += '&astrtCont=' + astrtCont	
        url += '&claimScope=' + claimScope	
        url += '&ipcNumber=' + ipcNumber	
        url += '&applicationNumber=' + applicationNumber	
        url += '&openNumber=' + openNumber	
        url += '&publicationNumber=' + publicationNumber	
        url += '&registerNumber=' + registerNumber	
        url += '&priorityApplicationNumber=' + priorityApplicationNumber	
        url += '&internationalApplicationNumber=' + internationalApplicationNumber	
        url += '&internationOpenNumber=' + internationOpenNumber	
        url += '&applicationDate=' + applicationDate	
        url += '&openDate=' + openDate	
        url += '&publicationDate=' + publicationDate	
        url += '&registerDate=' + registerDate	
        url += '&priorityApplicationDate=' + priorityApplicationDate	
        url += '&internationalApplicationDate=' + internationalApplicationDate	
        url += '&applicant=' + applicant	
        url += '&inventors=' + inventors	
        url += '&agent=' + agent	
        url += '&rightHoler=' + rightHoler	
        url += '&patent=' + patent	
        url += '&utility=' + utility	
        url += '&lastvalue=' + lastvalue	
        url += '&numOfRows=' + numOfRows	
        url += '&pageNo=' + pageNo	
        url += '&sortSpec=' + sortSpec	
        url += '&descSort=' + descSort	
        url += '&ServiceKey=' + self.key
        
        html = requests.get(url).text 
        root = BeautifulSoup(html, 'lxml-xml') 
        print(root)
        resultCode = root.find('resultCode').text
        if resultCode != '00':  
            msg = root.find('resultMag').text
            print(msg)
            return 

    # 항목별 검색 (자유 검색)
    def freeSearchInfo(self, word, docsStart, docsCount, sortSpec, descSort, patent, utility, lastvalue):
        url = 'http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/freeSearchInfo?'
        url += 'word=' + word # 자유 검색 
        url += '&docsStart=' + docsStart # 시작번호 (검색한 결과물의 출력할 번호)
        url += '&docsCount=' + docsCount # 조회건수(미입력시30건, 최대 60건)
        url += '&sortSpec=' + sortSpec # 정렬값(PD-공고일자, AD-출원일자, GD-등록일자, OPD-공개일자, FD-국제출원일자, FOD-국제공개일자, RD-우선권주장일자)
        url += '&descSort=' + descSort # 차순 (true-desc, false-asc)
        url += '&patent=' + patent # 특허 (포함 : true, 미포함 : false)
        url += '&utility=' + utility # 실용 (포함 : true, 미포함 : false)
        url += '&lastvalue=' + lastvalue  # 행정처분 (전체:공백입력, J:거절, R:등록, F:소멸, I:무효, C:취하, G:포기, A:공개)
        url += '&ServiceKey=' + self.key
        
        html = requests.get(url).text 
        root = BeautifulSoup(html, 'lxml-xml') 
        print(root)
        resultCode = root.find('resultCode').text
        if resultCode != '00':  
            msg = root.find('resultMag').text
            print(msg)
            return 
    
    # 항목별 검색 (출원번호 검색)
    def applicationNumberSearchInfo(self, applicationNumber, docsStart, docsCount, sortSpec, descSort, patent, utility, lastvalue):
        url = 'http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/applicationNumberSearchInfo?'
        url += 'applicationNumber=' + applicationNumber # 출원 번호 
        url += '&docsStart=' + docsStart # 시작번호 (검색한 결과물의 출력할 번호)
        url += '&docsCount=' + docsCount # 조회건수(미입력시30건, 최대 60건)
        url += '&sortSpec=' + sortSpec # 정렬값(PD-공고일자, AD-출원일자, GD-등록일자, OPD-공개일자, FD-국제출원일자, FOD-국제공개일자, RD-우선권주장일자)
        url += '&descSort=' + descSort # 차순 (true-desc, false-asc)
        url += '&patent=' + patent # 특허 (포함 : true, 미포함 : false)
        url += '&utility=' + utility # 실용 (포함 : true, 미포함 : false)
        url += '&lastvalue=' + lastvalue  # 행정처분 (전체:공백입력, J:거절, R:등록, F:소멸, I:무효, C:취하, G:포기, A:공개)
        url += '&ServiceKey=' + self.key
      
    # 항목별 검색 (CPC 검색) 
    def cpcSearchInfo(self, cpcNumber, docsStart, docsCount, sortSpec, descSort, patent, utility, lastvalue):
        url = 'http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/applicationNumberSearchInfo?'
        url += 'cpcNumber=' + cpcNumber # 출원 번호 
        url += '&docsStart=' + docsStart # 시작번호 (검색한 결과물의 출력할 번호)
        url += '&docsCount=' + docsCount # 조회건수(미입력시30건, 최대 60건)
        url += '&sortSpec=' + sortSpec # 정렬값(PD-공고일자, AD-출원일자, GD-등록일자, OPD-공개일자, FD-국제출원일자, FOD-국제공개일자, RD-우선권주장일자)
        url += '&descSort=' + descSort # 차순 (true-desc, false-asc)
        url += '&patent=' + patent # 특허 (포함 : true, 미포함 : false)
        url += '&utility=' + utility # 실용 (포함 : true, 미포함 : false)
        url += '&lastvalue=' + lastvalue  # 행정처분 (전체:공백입력, J:거절, R:등록, F:소멸, I:무효, C:취하, G:포기, A:공개)
        url += '&ServiceKey=' + self.key
        
        
if __name__ == "__main__": 
    s = Service()
    print(s.getWordSearch('센서', 0))
    print(s.getAdvancedSearch('발명', '센서'))
    print(s.freeSearchInfo('센서', 0))



