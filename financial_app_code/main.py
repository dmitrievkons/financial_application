from flask import Flask, render_template


financial_app = Flask(__name__)


@financial_app.route('/')
def index():
    return render_template('home.html', title='Home', content='OkPonChick')


@financial_app.route('/transactions')
def transactions():
    return render_template('transactions.html', title='Transactions', content='Textttt')


@financial_app.route('/categories')
def categories():
    return render_template('categories.html', title='Categories', content='Pon')


@financial_app.route('/information')
def info():
    return render_template('information.html', title='Info', content='oKKKKKKKKKKKKKKKKKkk')
