from flask import Flask, request, render_template, redirect, session
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

service = SearchService()
dbService = Service()
    
@app.route('/')
def root():
    if 'flag' not in session.keys():
        session['flag'] = False
        
    return render_template('index.html')

if __name__ == "__main__": 
    
    # 년도별 빈도수 많은 키워드 DB에 저장
    # for year in range(2017, 2022):
    #     tags = service.getYearKeywordSearch(year)
    #     print(tags)
        
    #     for keyword, num in tags:
    #         dbService.add(Keyword(year=year, keyword=keyword))
            
    # 분야별 특허가 가장 많은 출원인
    
    app.run(host = "127.0.0.1", port = 5000, debug = True)
    

    
    
