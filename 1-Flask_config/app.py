from flask import Flask 

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def hello_world():
    return '<h1>Hello World! This is Flask!</h1>'


if __name__ == '__main__':
    app.run()
    