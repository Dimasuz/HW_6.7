
from flask import jsonify, request
from flask.views import MethodView
# from app import app
from config import API_URL
from models import Session, Users, Adv


class UserView(MethodView):

    def get(self, user_id: int):
        with Session() as session:
            users = session.query(Users).get(user_id)
            return jsonify({'id': users.id})

    def post(self):
        user_data = request.json
        with Session() as session:
            new_user = Users(**user_data)
            session.add(new_user)
            session.commit()
            return jsonify({'id': new_user.id})



class AdvView(MethodView):

    def get(self, adv_id: int):
        with Session() as session:
            adv = session.query(Adv).get(adv_id)
            return jsonify({'id': adv.id})

    def post(self):
        adv_data = request.json
        with Session() as session:
            new_adv = Adv(**adv_data)
            session.add(new_adv)
            session.commit()
            return jsonify({'id': new_adv.id})

    def delete(self, adv_id: int):
        pass