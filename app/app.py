from flask import Flask

app = Flask('app')

from flask import jsonify

@app.route('/')
@app.route('/index')
def index():
    return jsonify({'hello': 'Hello, this is my homework Flask!'})

# from ..app import routes

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)