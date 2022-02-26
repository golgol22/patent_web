import pandas as pd
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


if __name__ == "__main__": 
    sf = SaveFile()
    # sf.year_ipc_patent()
    sf.year_keyword()