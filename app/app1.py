from flask import Flask
from flask_jwt_extended import JWTManager
import zhuce.zhuce as c
import deng.denglu as j
import talk.tell as r


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

users = {}


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

app.register_blueprint(c.j3)
app.register_blueprint(j.j1)
app.register_blueprint(r.j2)

if __name__ == '__main__':
    app.run()



