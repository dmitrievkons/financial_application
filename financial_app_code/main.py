from flask import Flask, render_template


financial_app = Flask(__name__)


@financial_app.route('/')
def index():
    return render_template('base.html')


@financial_app.route('/transactions')
def transactions():
    return 'pon'


@financial_app.route('/categories')
def categories():
    return 'ya lublu ponchiki'


@financial_app.route('/information')
def info():
    return 'Vot tak vot'
