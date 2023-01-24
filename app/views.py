from flask import jsonify, request
from flask.views import MethodView
from sqlalchemy.exc import IntegrityError
from app import app
from models import Session, Users, Adv
from errors import ApiError
from schema import CreateAdv, PatchAdv, validate


@app.errorhandler(ApiError)
def error_handler(error: ApiError):
    response = jsonify({"status": "error", "description": error.message})
    response.status_code = error.status_code
    return response

def get_item(session: Session, model_cls: Users | Adv, item_id: int) -> Users | Adv:
    item = session.query(model_cls).get(item_id)

    if item is None:
        raise ApiError(404, f'{model_cls.__name__.lower()} not found')
    return item


class UserView(MethodView):

    def get(self, user_id: int):
        with Session() as session:
            users = get_item(session, Users, user_id)
            return jsonify({'id': users.id})

    def post(self):
        user_data = request.json
        with Session() as session:
            new_user = Users(**user_data)
            session.add(new_user)
            try:
                session.commit()
            except IntegrityError:
                raise ApiError(status_cod=409, message='user is already exists')
            return jsonify({'id': new_user.id})


class AdvView(MethodView):

    def get(self, adv_id: int):
        with Session() as session:
            adv = get_item(session, Adv, adv_id)
            return jsonify({'id': adv.id, 'title': adv.title})

    def post(self):
        adv_data = validate(CreateAdv, request.json)
        with Session() as session:
            new_adv = Adv(**adv_data)
            session.add(new_adv)
            session.commit()
            return jsonify({'id': new_adv.id})

    def patch(self, adv_id: int):
        with Session() as session:
            params = validate(PatchAdv, request.json)
            adv = get_item(session, Adv, adv_id)
            print(jsonify({'title': adv.title}))
            for field, value in params.items():
                setattr(adv, field, value)
            print(jsonify(adv.title))
            session.add(adv)
            try:
                session.commit()
            except IntegrityError:
                raise ApiError(409, f"attr already exists")
            return jsonify({'id': adv.id})

    def delete(self, adv_id: int):
        with Session() as session:
            adv = get_item(session, Adv, adv_id)
            session.delete(adv)
            session.commit()
            return jsonify({'id': adv.id})


