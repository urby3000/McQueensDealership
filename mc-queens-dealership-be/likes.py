from flask import jsonify, Blueprint, request
from models import Like as ModelLike, db
from sqlalchemy import exc
from flask_login import login_required, current_user

likes_routes = Blueprint("likes", __name__)

@likes_routes.route("/like/create", methods=["POST"])
@login_required
def like_create():
    try:
        like = ModelLike(
            user_id = current_user.id,
            car_id = request.form.get("car_id"),
        )
        db.session.add(like)
        db.session.commit()
    except exc.SQLAlchemyError as e:
        return jsonify({"err": str(e.orig)})
    return jsonify(like)


@likes_routes.route("/like/<int:id>/delete", methods=["DELETE"])
@login_required
def like_delete(id):
    like = ModelLike.query.get_or_404(id)
    if not like.user_id == current_user.id:
        return jsonify({"err": ";P"})
    try:
        db.session.delete(like)
        db.session.commit()
        return jsonify({"status": "success"})
    except exc.SQLAlchemyError as e:
        return jsonify({"err": str(e.orig)})