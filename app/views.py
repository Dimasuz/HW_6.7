from flask.views import MethodView
from app import app
import requests
from config import API_URL

class Views(MethodView):

    def get(self):
        respones = requests.get(API_URL)
        return respones.json()

    def post(self):
        pass


app.add_url_rule('views', view_func=Views.as_view(), methods=['GET', 'POST'])