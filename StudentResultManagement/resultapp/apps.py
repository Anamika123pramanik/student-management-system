from django.apps import AppConfig


class ResultappConfig(AppConfig):
    name = 'resultapp'


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/computer')
def computer():
    return render_template('computer.html')





