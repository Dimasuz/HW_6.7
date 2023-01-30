from flask import jsonify
from views import UserView, AdvView
from app import app


@app.route('/')
@app.route('/index/')
def index():
    return jsonify({'hello': 'Hello, this is my homework Flask!'})


app.add_url_rule('/users/', view_func=UserView.as_view('user_add'), methods=['POST'])
app.add_url_rule('/users/<int:user_id>/', view_func=UserView.as_view('user'), methods=['GET', 'DELETE'])

app.add_url_rule('/adv/', view_func=AdvView.as_view('adv_add'), methods=['POST'])
app.add_url_rule('/adv/<int:adv_id>/', view_func=AdvView.as_view('adv'), methods=['GET', 'PATCH', 'DELETE'])


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)