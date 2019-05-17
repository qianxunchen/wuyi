from flask import request, jsonify,Blueprint

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

j3 = Blueprint('j3',__name__)

users = {}

@j3.route('/signup', methods=['POST'])
def signup():
    if not request.is_json:
        return jsonify({"提示": "没有json请求"}), 400
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"提示": "缺少用户名"}), 400
    if not password:
        return jsonify({"提示": "缺少密码"}), 400
    if username in users:
        return jsonify({"提示": "这个用户名已被注册"}), 201
    users[username] = User(username,password)
    return jsonify({"提示": "注册成功!"}), 200