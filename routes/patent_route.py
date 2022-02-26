from email.policy import default
import os
from flask import request, render_template, redirect, Blueprint, session, json, jsonify

from patent_office.vo import Office
from patent_office.service import Service as office_service
from patent_office.service import DBService as office_DB_service

from patent_news.vo import News
from patent_news.service import Service as news_service
from patent_news.service import DBService as news_DB_service


office_service = office_service()
office_DB_service = office_DB_service()

news_service = news_service()
news_DB_service = news_DB_service()

bp = Blueprint('patent', __name__, url_prefix='/patent')

# 특허 검색 메뉴
@bp.route('/search')
def search():
    return render_template('patent/search.html')

@bp.route('/search_action')
def search_action():
    return render_template('patent/search.html')

# 특허 사무소
@bp.route('/office')
def office():
    res = office_service.getPatentOffice('전체')
    res = enumerate(res)
    return render_template('patent/office.html', res=res)

@bp.route('/office_search', methods=['POST'])
def office_search():
    data = json.loads(request.data)
    search =  data.get('search')
    res = office_service.getPatentOffice(search)
    return jsonify(result=json.dumps(res, default=str))

@bp.route('/fav_add_office', methods=['POST'])
def fav_add_office():
    data = json.loads(request.data)
    data =  data.get('data')
    data = str(data)
    split_data = data.split('|')
    office_DB_service.add(Office(split_data[0], split_data[1], split_data[2], split_data[3]))
    return jsonify(result=1)

# 특허 뉴스
@bp.route('/news')
def news():
    news = news_service.getPatentNews()
    news = enumerate(news)
    return render_template('patent/news.html', news=news)

@bp.route('/news_search', methods=['POST'])
def news_search():
    data = json.loads(request.data)
    search =  data.get('search')
    res =  news_service.getPatentNews(section=search)
    return jsonify(result=json.dumps(res, default=str))

@bp.route('/fav_add_news', methods=['POST'])
def fav_add_news():
    data = json.loads(request.data)
    data =  data.get('data')
    data = str(data)
    split_data = data.split('|')
    news_DB_service.add(News(split_data[0], split_data[1], split_data[2], split_data[3], split_data[4], split_data[5]))
    return jsonify(result=1)

# 출원서&명세서
@bp.route('/document')
def document():
    return render_template('patent/document.html')

# 파일 다운로드
@bp.route('/download', methods = ['GET', 'POST'])
def download_file():
    files_list = os.listdir("uploads")
    if request.method == 'POST':
        sw = 0
        for x in files_list:
            if(x == request.form['file']):
                sw = 1
        try:
            path = "./uploads/"
            return send_file(path + request.form['file'],
                    download_name = request.form['file'],
                    as_attachment=True)
        except:
            print("download error")
    return render_template('download.html', files=files_list)

# 특허단어찾기
@bp.route('/search_word')
def search_word():
    return render_template('patent/search_word.html')