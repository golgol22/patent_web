from email.policy import default
from flask import request, render_template, redirect, Blueprint, session, json, jsonify
from patent_office.service import Service

service = Service()
bp = Blueprint('patent', __name__, url_prefix='/patent')

@bp.route('/office')
def office():
    res = service.getPatentOffice('전체')
    res = enumerate(res)
    return render_template('patent/office.html', res=res)

@bp.route('/office_search', methods=['POST'])
def office_search():
    data = json.loads(request.data)
    search =  data.get('search')
    res = service.getPatentOffice(search)
    return jsonify(result=json.dumps(res, default=str))

@bp.route('/search')
def search():
    return render_template('patent/search.html')

@bp.route('/search_action')
def search_action():
    return render_template('patent/search.html')