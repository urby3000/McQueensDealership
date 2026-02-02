from flask import jsonify, Blueprint, request
from models import User as ModelUser, db
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import exc

users_routes = Blueprint("users", __name__)

# @users_routes.route("/user/<int:id>")
# def user_detail(id: int):
#     return jsonify(ModelUser.query.get_or_404(id))

@users_routes.route("/user/create", methods=["POST"])
@login_required
def user_create():
    if not current_user.is_admin:
        return jsonify({"err":"You don't have admin rights."})
    try:
        email_form=request.form.get("email")
        password_form=request.form.get("password")
        is_admin_form=False
        if request.form.get("is_admin") == "1":
            is_admin_form = True
        if ModelUser.query.filter_by(email=email_form).first():
            return jsonify({"err":"Email already in use."})

        hashed_password = generate_password_hash(password_form, method="pbkdf2:sha256")

        user = ModelUser(email=email_form, password=hashed_password, is_admin=is_admin_form)
        db.session.add(user)
        db.session.commit()
    except exc.SQLAlchemyError as e:
        return jsonify({"err": str(e.orig)})
    return jsonify(user)

@users_routes.route("/user/login", methods=["POST"])
def login():
    email_form = request.form.get("email")
    password_form = request.form.get("password")

    user = ModelUser.query.filter_by(email=email_form).first()

    if user and check_password_hash(user.password, password_form):
        login_user(user)
        return jsonify(user)
    else:
        return jsonify({"err":"Invalid email or password"})

@users_routes.route("/user/logout")
@login_required
def logout():
    logout_user()
    return jsonify({"msg":"Logged out."})