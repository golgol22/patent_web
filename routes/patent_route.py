from email.policy import default
from flask import request, render_template, redirect, Blueprint, session, json, jsonify
from patent_office.service import Service as office_service
from patent_news.service import Service as news_service

office_service = office_service()
news_service = news_service()

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