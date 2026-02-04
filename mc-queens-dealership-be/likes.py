from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask import jsonify, Blueprint, request
from models import Car as ModelCar, User as ModelUser, Like as ModelLike, db
from sqlalchemy import exc

likes_routes = Blueprint("likes", __name__)

@likes_routes.route("/car/<int:id>/like", methods=["GET"])
@jwt_required()
def like_create(id):
    try:
        current_user = ModelUser.query.filter_by(email=get_jwt_identity()).first()
        like = ModelLike(
            user_id = current_user.id,
            car_id = ModelCar.query.get_or_404(id).id,
        )
        if not ModelLike.query.filter_by(user_id=current_user.id,car_id=id).first():
            db.session.add(like)
            db.session.commit()
            return jsonify({"msg": "success"})
    except exc.SQLAlchemyError as e:
        return jsonify({"err": str(e.orig)})
    return jsonify({"msg": "ok"})


@likes_routes.route("/car/<int:id>/unlike", methods=["DELETE"])
@jwt_required()
def like_delete(id):
    # like = ModelLike.query.get_or_404(id)
    current_user = ModelUser.query.filter_by(email=get_jwt_identity()).first()
    like = ModelLike.query.filter_by(user_id=current_user.id,car_id=id).first()
    try:
        if like:
            db.session.delete(like)
            db.session.commit()
            return jsonify({"msg": "success"})
        return jsonify({"msg": "ok"})
    except exc.SQLAlchemyError as e:
        return jsonify({"err": str(e.orig)})