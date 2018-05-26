from flask import render_template, request
from my_app import app

@app.route('/')
@app.route('/hello')
def hello_world():
    user = request.args.get('user', 'Ashirwad')
    return render_template('index.html', user=user)