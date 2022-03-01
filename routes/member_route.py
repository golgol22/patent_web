from flask import request, render_template, redirect, Blueprint, session, json, jsonify
from datetime import datetime
from member.vo import Member, MyCal
from member.service import Service, AddCal

from patent_search.service import DBService as field_DB_service

from patent_search.service import FavPatentDBService as patent_DB_service

from patent_office.vo import Office
from patent_office.service import Service as office_service
from patent_office.service import DBService as office_DB_service

from patent_news.vo import News
from patent_news.service import Service as news_service
from patent_news.service import DBService as news_DB_service

service = Service() # Member

field_DB_service = field_DB_service()
patent_DB_service = patent_DB_service()
office_DB_service = office_DB_service()
news_DB_service = news_DB_service()
addCal = AddCal()

bp = Blueprint('member', __name__, url_prefix='/member')

@bp.route('/signup_agree')
def signup_agree():
    return render_template('member/signup_agree.html')

@bp.route('/signup_input', methods=['POST'])
def signup_input():
    return render_template('member/signup_input.html')

@bp.route('/signup_id_check', methods=['POST'])
def signup_id_check():
    data = json.loads(request.data)
    id = data.get('id')
    result = 0
    if service.selectById(id) == None:
        result = 2 # id 중복 X
    else:
        result = 1
    
    return jsonify(result=result)

@bp.route('/signup_input_action', methods=['POST'])
def signup_input_action():
    data = json.loads(request.data)
    id =  data.get('id')
    pwd =  data.get('pw')
    name =  data.get('name')
    tel =  data.get('tel')
    service.join(Member(id=id, pwd=pwd, name=name, tel=tel))
    return jsonify(result=2)

@bp.route('/login')
def login():
    return render_template('member/login.html')

@bp.route('/login_action', methods=['POST'])
def login_action():
    data = json.loads(request.data)
    id =  data.get('id')
    pwd =  data.get('pw')
    flag = service.login(id, pwd)
    return jsonify(result=flag)

@bp.route('/logout')
def logout():
    service.logout()
    return redirect('/')

@bp.route('/mypage')
def mypage():
    # 관심분야 등록
    f = field_DB_service.getById()
    
    # 찜한 특허 
    res_patent = patent_DB_service.getById()
    
    # 찜한 사무소
    res_office = office_DB_service.getById()
    
    # 찜한 뉴스
    res_news = news_DB_service.getById()
    
    # 오늘 날짜 구하기 
    date = datetime.today().strftime("%Y년 %m월 %d일")  
    date_month = datetime.today().strftime("%Y.%m")
    
    # 출원일 구하기
    application_date = addCal.getById()
    
    # 회원정보
    m:Member = service.myInfo()
    return render_template('member/mypage.html', f=f, res_patent=res_patent, res_office=res_office, res_news=res_news, 
        date=date, date_month=date_month, application_date=application_date, m=m)

@bp.route('/user_fav_field', methods=['POST'])
def user_fav_field():
    data = json.loads(request.data)
    f_name =  data.get('data')
    f = field_DB_service.getById()
    if f == None: 
        field_DB_service.add(f_name)
    else:
        field_DB_service.edit(f_name)
    return jsonify(result=1)

@bp.route('/add_application_date', methods=['POST'])
def add_application_date():
    data = json.loads(request.data)
    date =  data.get('data')
    f = addCal.getById()
    if f == None: 
        addCal.add(date)
    else:
        addCal.edit(date)
    return jsonify(result=1)

@bp.route('/user_info_update', methods=['POST'])
def user_info_update():
    data = json.loads(request.data)
    pwd =  data.get('pw')
    name =  data.get('name')
    tel =  data.get('tel')
    m:Member = service.editMyInfo(pwd, name, tel)
    return jsonify(result=1)

@bp.route('/out')
def out():
    service.out()
    return render_template('index.html')

