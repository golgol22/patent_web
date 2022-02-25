from flask import Flask, request, render_template, redirect, session
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='NanumBarunGothic')
plt.rc('axes', unicode_minus=False)

from member.vo import db, migrate
import routes.member_route as mr
import routes.patent_route as pr

from patent_search.service import SearchService, Service
from patent_search.vo import Keyword
from member.vo import db

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

service = SearchService() # 검색 
dbService = Service() # 년도별 키워드 저장 DB
    
@app.route('/')
def root():
    if 'flag' not in session.keys():
        session['flag'] = False
       
    # == 파일에 값 저장하기 (값을 다시 불러올 경우에만 주석해제하고 사용)==
    # 년도별 빈도수 많은 키워드 DB에 저장
    # for year in range(2017, 2022):
    #     tags = service.getYearKeywordSearch(year)
    #     print(tags)
        
    #     for keyword, num in tags:
    #         dbService.add(Keyword(year=year, keyword=keyword))
    
    # 년도별 키워드 DB에서 불러오기 
    res_2017 = dbService.getByAll(2017)
    res_2017 = enumerate(res_2017)
    res_2018 = dbService.getByAll(2018)
    res_2018 = enumerate(res_2018)
    res_2019 = dbService.getByAll(2019)
    res_2019 = enumerate(res_2019)
    res_2020 = dbService.getByAll(2020)
    res_2020 = enumerate(res_2020)
    res_2021 = dbService.getByAll(2021)
    res_2021 = enumerate(res_2021)
   
    # 오늘 날짜 구하기 
    date = datetime.today().strftime("%Y년 %m월 %d일")  
    
    # 년도별 분야별 특허 출원수 그래프 그리기
    year_ipc_patent = pd.read_csv('year_ipc_patent.csv', index_col=0, encoding='euc-kr')
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
        
    return render_template('index.html', date=date, year_ipc_ranking_data=year_ipc_ranking_data, img_path=img_path,
        res_2017=res_2017, res_2018=res_2018, res_2019=res_2019, res_2020=res_2020, res_2021=res_2021)


if __name__ == "__main__": 
    app.run(host = "127.0.0.1", port = 5000, debug = True)
    

    
    
