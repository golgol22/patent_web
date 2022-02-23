from flask import Flask, request, render_template, redirect, session
from patent_search.service import Service
# from member.vo import db, migrate
# import routes.mem_route as mr
# import routes.board_route as br

import config   # 컨피그 파일(config.py) import

# 플라스크 객체 생성
app = Flask(__name__)

# 시크릿 키 생성
app.secret_key = 'everything'

# 플라스크 컨피그에 사용자정의 컨피그 추가
app.config.from_object(config)

# 블루 프린트 등록
# app.register_blueprint(mr.bp)
# app.register_blueprint(br.bp)

# ORM 연동
# db.init_app(app)
# migrate.init_app(app, db)

# @app.route('/')
# def root():
#     if 'flag' not in session.keys():
#         session['flag'] = False
#     return render_template('index.html')


if __name__ == "__main__": 
    s = Service()
    # app.run(host = "127.0.0.1", port = 5000, debug = True)
