from flask import jsonify, Blueprint, request
from models import Like as ModelLike, db
from sqlalchemy import exc

likes_routes = Blueprint("likes", __name__)

@likes_routes.route("/like/create", methods=["POST"])
def like_create():
    try:
        like = ModelLike(
            user_id = request.form["user_id"],
            car_id = request.form["car_id"],
        )
        db.session.add(like)
        db.session.commit()
    except exc.SQLAlchemyError as e:
        return jsonify({"err": str(e.orig)})
    return jsonify(like)


@likes_routes.route("/like/<int:id>/delete", methods=["DELETE"])
def like_delete(id):
    like = ModelLike.query.get_or_404(id)
    try:
        db.session.delete(like)
        db.session.commit()
        return jsonify({"status": "success"})
    except exc.SQLAlchemyError as e:
        return jsonify({"err": str(e.orig)})