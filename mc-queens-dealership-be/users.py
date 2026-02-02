from flask import jsonify, Blueprint, request
from models import User as ModelUser, db
from sqlalchemy import exc

users_routes = Blueprint("users", __name__)

@users_routes.route("/user/<int:id>")
def user_detail(id: int):
    return jsonify(db.session.query(ModelUser).get(id))

@users_routes.route("/user/create", methods=["POST"])
def user_create():
    try:
        user = ModelUser(
            email=request.form["email"],
            password=request.form["password"],
        )
        db.session.add(user)
        db.session.commit()
    except exc.SQLAlchemyError as e:
        return jsonify({"err": str(e.orig)})
    return jsonify(user)