from flask import request, render_template, redirect, Blueprint, session, json, jsonify
from member.vo import Member
from member.service import Service

service = Service()
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
    return render_template('index.html')

@bp.route('/out')
def out():
    service.out()
    return render_template('index.html')

