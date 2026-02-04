from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask import jsonify, Blueprint, request
from models import User as ModelUser, db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import exc

users_routes = Blueprint("users", __name__)

# @users_routes.route("/user/<int:id>")
# def user_detail(id: int):
#     return jsonify(ModelUser.query.get_or_404(id))

@users_routes.route("/user/create", methods=["POST"])
def user_create():
    try:
        email_form=request.form.get("email")
        password_form=request.form.get("password")
        is_admin_form=False
        
        if ModelUser.query.filter_by(email=email_form).first():
            return jsonify({"err":"Email already in use."})

        hashed_password = generate_password_hash(password_form, method="pbkdf2:sha256")

        user = ModelUser(email=email_form, password=hashed_password, is_admin=is_admin_form)
        db.session.add(user)
        db.session.commit()
    except exc.SQLAlchemyError as e:
        return jsonify({"err": str(e.orig)})
    return jsonify({"msg":"success"})

@users_routes.route("/user/login", methods=["POST"])
def login():
    email_form = request.form.get("email")
    password_form = request.form.get("password")

    user = ModelUser.query.filter_by(email=email_form).first()

    if user and check_password_hash(user.password, password_form):
        access_token = create_access_token(identity=user.email)
        return jsonify(access_token=access_token, email=email_form, is_admin=user.is_admin, user_id=user.id)
    else:
        return jsonify({"err":"Invalid email or password"})

@users_routes.route("/user/logout")
@jwt_required()
def logout():
    return jsonify({"msg":"Logged out."})