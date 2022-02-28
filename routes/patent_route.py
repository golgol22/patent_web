from email.policy import default
import os
import pandas as pd
from flask import request, render_template, redirect, Blueprint, session, json, jsonify

from patent_search.vo import WordSearch
from patent_search.service import SearchService as search_office
from patent_search.service import DBService as search_DB_service
from patent_search.service import FavPatentDBSservice as favPatentDBSservice

from patent_office.vo import Office
from patent_office.service import Service as office_service
from patent_office.service import DBService as office_DB_service

from patent_news.vo import News
from patent_news.service import Service as news_service
from patent_news.service import DBService as news_DB_service

search_office = search_office()
search_DB_service = search_DB_service()
favPatentDBSservice = favPatentDBSservice()

office_service = office_service()
office_DB_service = office_DB_service()

news_service = news_service()
news_DB_service = news_DB_service()

bp = Blueprint('patent', __name__, url_prefix='/patent')

# 특허 검색 메뉴
@bp.route('/search')
def search():
    search_result_covid = pd.read_csv('static/csv/search_result_covid.csv', engine='python')
    res_covid = search_result_covid[search_result_covid['등록상태'] == '등록'].values.tolist()
    res_covid = enumerate(res_covid)
    return render_template('patent/search.html', res_covid=res_covid)

@bp.route('/reg_search_action', methods=['POST'])
def reg_search_action():
    data = json.loads(request.data)
    search =  data.get('search')
    search_result_covid = pd.read_csv('static/csv/search_result_covid.csv', engine='python')
    res_covid = search_result_covid[search_result_covid['등록상태'] == search].values.tolist()
    print(res_covid)
    res = []
    for covid in res_covid:
        res.append(WordSearch(covid[0], covid[1], covid[2], covid[3], covid[4], covid[5], 
            covid[6], covid[7], covid[8], covid[9], covid[10], covid[11], covid[12], 
            covid[13], covid[14], covid[15]))
    return jsonify(result=json.dumps(res, default=str))

@bp.route('/word_search_action', methods=['POST'])
def word_search_action():
    data = json.loads(request.data)
    search =  data.get('search')
    # search_result_covid = pd.read_csv('static/csv/search_result_covid.csv', engine='python')
    # res_covid = search_result_covid[search_result_covid['등록상태'] == search].values.tolist()
    # res_covid = enumerate(res_covid)
    # return jsonify(result=json.dumps(res_covid, default=str))

@bp.route('/fav_add_patent', methods=['POST'])
def fav_add_patent():
    data = json.loads(request.data)
    data =  data.get('data')
    split_data = list(data)
    favPatentDBSservice.add(WordSearch(split_data[0], split_data[1], split_data[2], split_data[3], 
        split_data[4], split_data[5], split_data[6], split_data[7], split_data[8], split_data[9], split_data[10],
        split_data[11], split_data[12], split_data[13], split_data[14], split_data[15]))
    return jsonify(result=1)

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

# 특허단어찾기
@bp.route('/search_word')
def search_word():
    return render_template('patent/search_word.html')