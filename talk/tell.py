from flask import Blueprint

j2 = Blueprint('j2',__name__)

@j2.route('/tell',methods = ['POST'])
def tell():
    return'荣你来啦！'