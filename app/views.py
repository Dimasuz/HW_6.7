import flask_bcrypt
from flask import jsonify, request
from flask.views import MethodView
from sqlalchemy.exc import IntegrityError
from app import app
from models import Session, Users, Adv
from errors import ApiError
from schema import CreateAdv, PatchDelAdv, validate


bcrypt = flask_bcrypt.Bcrypt(app)


def hash_password(password: str) -> str:
    return bcrypt.generate_password_hash(password.encode()).decode()


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


def check_user(session: Session, adv_user_id=0, **item_data):

    if 'password' in item_data:
        user = get_item(session, Users, item_data['user_id'])
        if adv_user_id == 0:
            adv_user_id = user.id
        if bcrypt.check_password_hash(user.password, item_data['password']) and adv_user_id == user.id:
            item_data.pop('password')
            return item_data
        else:
            raise ApiError(401, "wrong user_id or password")


class UserView(MethodView):

    def get(self, user_id: int):
        with Session() as session:
            users = get_item(session, Users, user_id)
            return jsonify({'id': users.id})

    def post(self):
        user_data = request.json
        with Session() as session:
            #
            user_data['password'] = hash_password(user_data['password'])
            #
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
            return jsonify({'id': adv.id,
                            'title': adv.title,
                            'descr': adv.descr,
                            'creat_time': adv.creat_time.isoformat(),
                            'user_id': adv.user_id
                            })

    def post(self):
        data = validate(CreateAdv, request.json)
        with Session() as session:
            adv_data = check_user(session, **data)
            new_adv = Adv(**adv_data)
            session.add(new_adv)
            session.commit()
            return jsonify({'id': new_adv.id})

    def patch(self, adv_id: int):
        with Session() as session:
            adv_data = validate(PatchDelAdv, request.json)
            adv = get_item(session, Adv, adv_id)
            adv_data = check_user(session, adv.user_id, **adv_data)
            for field, value in adv_data.items():
                setattr(adv, field, value)
            session.add(adv)
            try:
                session.commit()
            except IntegrityError:
                raise ApiError(409, f"attr already exists")
            return jsonify({'id': adv.id})

    def delete(self, adv_id: int):
        with Session() as session:
            adv_data = validate(PatchDelAdv, request.json)
            adv = get_item(session, Adv, adv_id)
            check_user(session, adv.user_id, **adv_data)
            session.delete(adv)
            session.commit()
            return jsonify({'id': adv.id})
