import pandas as pd
from vo import WordSearch
from service import SearchService


class SaveFile:
    
    def __init__(self): 
        self.service = SearchService()
        
    # 년도별 분야별 특허 출원수 구하기
    def year_ipc_patent(self):
        ipcs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        total_data = []
        for year in range(2017, 2022):
            term = str(year) + '0101~' + str(year) + '1231'
            num_data = []
            for ipc in ipcs:
                res, numOfRows, pageNo, totalCount = self.service.getAdvancedSearch(ipcNumber=ipc, applicationDate=term) 
                print(str(year) + "년 " +  ipc + "분야의 특허 출원수: " + str(totalCount))
                num_data.append(totalCount)
            total_data.append(num_data)
            
        data = pd.DataFrame(total_data, 
                index=['2017', '2018', '2019', '2020', '2021'], 
                columns=['생활(A)', '운송(B)', '화학(C)', '섬유(D)', '구조(E)', '기계(F)', '물리(G)', '전기(H)'])
        data.to_csv('static/csv/year_ipc_patent.csv', index='년도', encoding='euc-kr')
        
    
    # 년도별 빈도수 많은 키워드 DB에 저장
    def year_keyword(self):
        total_data = []
        for year in range(2017, 2022):
            tags = self.service.getYearKeywordSearch(year)
            print(tags)
            row_data = []
            for keyword, num in tags:
                row_data.append(year)
                row_data.append(keyword)
                row_data.append(num)
            total_data.append(row_data)
            
        data = pd.DataFrame(total_data, 
                columns=['년도', '단어', '빈도수'])
        data.to_csv('static/csv/year_keyword.csv', index=False, encoding='euc-kr')    


    def search_result_covid(self):
        # 코로나, covid 
        total_data = []
        for pageNo in range(0, 1):
            res_patent, numOfRows, pageNo, totalCount = self.service.getAdvancedSearch(inventionTitle='코로나', sortSpec='AD', descSort='true', numOfRows=500, pageNo=pageNo)
            for patent in res_patent:
                row_data = []
                row_data.append(patent.__getattribute__('indexNo'))
                row_data.append(patent.__getattribute__('registerStatus'))
                row_data.append(patent.__getattribute__('inventionTitle'))
                row_data.append(patent.__getattribute__('ipcNumber'))
                row_data.append(patent.__getattribute__('registerNumber'))
                row_data.append(patent.__getattribute__('registerDate'))
                row_data.append(patent.__getattribute__('applicationNumber'))
                row_data.append(patent.__getattribute__('applicationDate'))
                row_data.append(patent.__getattribute__('openNumber'))
                row_data.append(patent.__getattribute__('openDate'))
                row_data.append(patent.__getattribute__('publicationNumber'))
                row_data.append(patent.__getattribute__('publicationDate'))
                row_data.append(patent.__getattribute__('astrtCont'))
                row_data.append(patent.__getattribute__('bigDrawing'))
                row_data.append(patent.__getattribute__('drawing'))
                row_data.append(patent.__getattribute__('applicantName'))
                print(row_data)
                total_data.append(row_data)
                
        data = pd.DataFrame(total_data, 
            columns=['일련번호', '등록상태', '발명의 명칭', 'IPC 번호', '등록번호', '등록일자', '출원번호', '출원일자', '공개번호', '공개일자', '공고번호', '공고일자', '초록', '큰 이미지 경로', '이미지 경로', '출원인'])
        data.to_csv('static/csv/search_result_covid.csv', index=False, encoding='utf-8')  

    def search_detail_classification_G(self): # 물리(G)
        ipcs = ['G01', 'G02', 'G03'] # 물리 상세 분야 
        total_data = []
        for ipc in ipcs:
            res_patent, numOfRows, pageNo, totalCount = self.service.getAdvancedSearch(ipcNumber=ipc, numOfRows=10)
            print(ipc + "분야의 특허 출원수: " + str(totalCount))
            total_data.append(totalCount)
            
        data = pd.DataFrame(total_data, 
            columns=['생활(A)', '운송(B)', '화학(C)', '섬유(D)', '구조(E)', '기계(F)', '물리(G)', '전기(H)']) # 상세분야 
        data.to_csv('static/csv/year_ipc_detail_patent_G.csv', index='년도', encoding='euc-kr')

if __name__ == "__main__": 
    sf = SaveFile()
    # sf.year_ipc_patent()
    # sf.year_keyword()
    # sf.search_result_covid()
    sf.search_detail_classification_G()