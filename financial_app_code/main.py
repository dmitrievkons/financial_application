from flask import Flask


financial_app = Flask(__name__)


@financial_app.route('/')
def index():
    return 'Hi'


@financial_app.route('/transactions')
def transactions():
    return 'pon'


@financial_app.route('/categories')
def categories():
    return 'ya lublu ponchiki'
