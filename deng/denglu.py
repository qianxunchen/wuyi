from flask_jwt_extended import create_access_token
from flask import jsonify, request, Blueprint
import zhuce.zhuce as jin

j1 = Blueprint('j1',__name__)

@j1.route('/login', methods = ['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg":"没有json请求"}), 400
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if ( not username ) or ( not password):
        return jsonify({"msg":"用户名或密码没有参数"}), 400
    loginuser = jin.users.get(username,None)#在users里取出username
    if not loginuser:
        return jsonify({"msg": "用户不存在"})
    elif loginuser.password == password:
        return jsonify(令牌=create_access_token(identity=username)), 200
    else:
        return jsonify({"msg": "用户名或密码不正确"}), 401
