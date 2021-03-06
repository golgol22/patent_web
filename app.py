from flask import Flask, request, render_template, redirect, session
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# 그래프 한글깨짐 방지
plt.rc('font', family='NanumBarunGothic')
plt.rc('axes', unicode_minus=False)

from member.vo import db, migrate
import routes.member_route as mr
import routes.patent_route as pr

from patent_search.service import SearchService as search_service
from patent_search.vo import Field
from patent_search.service import DBService as field_DB_service
from patent_search.service import SearchRankingDB as SearchRankingDB

search_service = search_service()
field_DB_service = field_DB_service()
SearchRankingDB = SearchRankingDB()

import config   # 컨피그 파일(config.py) import

# 플라스크 객체 생성
app = Flask(__name__)

# 시크릿 키 생성
app.secret_key = 'everything'

# 플라스크 컨피그에 사용자정의 컨피그 추가
app.config.from_object(config)

# 블루 프린트 등록
app.register_blueprint(mr.bp)
app.register_blueprint(pr.bp)

# ORM 연동
db.init_app(app)
migrate.init_app(app, db)

@app.route('/')
def root():
    if 'flag' not in session.keys():
        session['flag'] = False
   
    # 오늘 날짜 구하기 
    date = datetime.today().strftime("%Y년 %m월 %d일")    
    
    # 검색 키워드 순위
    res_search = SearchRankingDB.getByTop5()
    res_search = enumerate(res_search)
    
    # 년도별 분야별 특허 출원수 그래프 그리기
    year_ipc_patent = pd.read_csv('static/csv/year_ipc_patent.csv', index_col=0, encoding='euc-kr')
    img_path = 'static/images/year_ipc_patent.png'
    plt.figure(figsize=(8, 6))
    plt.xticks([2017, 2018, 2019, 2020, 2021])
    plt.plot(year_ipc_patent, '-o', label=year_ipc_patent.columns)
    plt.legend(loc='best')
    plt.xlabel("년도")
    plt.ylabel("출원수")
    plt.savefig(img_path)
    
    # 분야별 특허 출원 순위
    field = ['생활(A)', '운송(B)', '화학(C)', '섬유(D)', '구조(E)', '기계(F)', '물리(G)', '전기(H)']
    year_ipc_ranking_data = {}
    for i in range(0, len(field)):
        year_ipc_ranking_data[field[i]] = year_ipc_patent[field[i]].sum()
    
    year_ipc_ranking_data = sorted(year_ipc_ranking_data.items(), key=lambda x: x[1], reverse=True)
    year_ipc_ranking_data = enumerate(year_ipc_ranking_data)
        
    # 년도별 주요 키워드
    years = [2017, 2018, 2019, 2020, 2021]
    year_keyword = pd.read_csv('static/csv/year_keyword.csv', encoding='euc-kr')
    for year in years:
        globals()[f'res_{year}'] = year_keyword[year_keyword['년도'] == year].values.tolist()
        globals()[f'res_{year}'] = enumerate(globals()[f'res_{year}'])
               
    # 로그인이 되어있고 관심분야가 등록되어 있으면 관심분야에 대한 분석도 제공
    res_lately_patent_R = []
    res_lately_patent_G = []
    
    filepath = 'static/csv/'
    fav_field = None
    if session['flag']:
        fav_field =  field_DB_service.getById()
        if fav_field != None:
            if fav_field.field_name == '생활(A)':
                filepath = filepath + 'A/'
                ipcNumber = 'A'
            if fav_field.field_name == '운송(B)':
                filepath = filepath + 'B/'
                ipcNumber = 'B'
            if fav_field.field_name == '화학(C)':
                filepath = filepath + 'C/'
                ipcNumber = 'C'
            if fav_field.field_name == '섬유(D)':
                filepath = filepath + 'D/'
                ipcNumber = 'D'
            if fav_field.field_name == '구조(E)':
                filepath = filepath + 'E/'
                ipcNumber = 'E'
            if fav_field.field_name == '기계(F)':
                filepath = filepath + 'F/'
                ipcNumber = 'F'
            if fav_field.field_name == '물리(G)':
                filepath = filepath + 'G/'
                ipcNumber = 'G'
            if fav_field.field_name == '전기(H)':
                filepath = filepath + 'H/'
                ipcNumber = 'H'
                
            res_lately_patent_R, numOfRows, pageNo, totalCount = search_service.getAdvancedSearch(ipcNumber=ipcNumber, lastvalue='R', sortSpec='AD', descSort='true', numOfRows=3)
            res_lately_patent_G, numOfRows, pageNo, totalCount = search_service.getAdvancedSearch(ipcNumber=ipcNumber, lastvalue='G', sortSpec='AD', descSort='true', numOfRows=3)
    
    # 년도별 주요 키워드
    years = [2017, 2018, 2019, 2020, 2021]
    for year in years:
        globals()[f'res_detail_{year}'] = []
        
    if fav_field != None:
        year_detail_keyword = pd.read_csv(filepath + 'year_detail_keyword.csv', encoding='euc-kr')
        for year in years:
            globals()[f'res_detail_{year}'] = year_detail_keyword[year_detail_keyword['년도'] == year].values.tolist()
            globals()[f'res_detail_{year}'] = enumerate(globals()[f'res_detail_{year}'])
    
    # 변수명 자동 생성으로 인한 경고
    return render_template('index.html', res_search=res_search, fav_field=fav_field, date=date,
            year_ipc_ranking_data=year_ipc_ranking_data, img_path=img_path,
            res_2017=res_2017, res_2018=res_2018, res_2019=res_2019, res_2020=res_2020, res_2021=res_2021,
            res_detail_2017=res_detail_2017, res_detail_2018=res_detail_2018, res_detail_2019=res_detail_2019, res_detail_2020=res_detail_2020, res_detail_2021=res_detail_2021,
            res_lately_patent_R=res_lately_patent_R, res_lately_patent_G=res_lately_patent_G, field_name=fav_field)


if __name__ == "__main__": 
    app.run(host = "127.0.0.1", port = 5000, debug = True)
    

    
    
