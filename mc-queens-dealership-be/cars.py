from flask import jsonify, Blueprint, request
from models import Car as ModelCar, db
from sqlalchemy import exc
from flask_login import login_required, current_user

cars_routes = Blueprint("cars", __name__)

@cars_routes.route("/cars")
def cars():
    return jsonify(ModelCar.query.all())

@cars_routes.route("/car/<int:id>")
def car_detail(id: int):
    return jsonify(ModelCar.query.get_or_404(id))

@cars_routes.route("/car/create", methods=["POST"])
@login_required
def car_create():
    if not current_user.is_admin:
        return jsonify({"err":"You don't have admin rights."})
    try:
        car = ModelCar(
            brand = request.form.get("brand"),
            model = request.form.get("model"),
            year = request.form.get("year"),
            price = request.form.get("price"),
            fuel_type = request.form.get("fuel_type"),
            doors = request.form.get("doors"),
            description = request.form.get("description"),
            # img = request.form["img"]
        )
        db.session.add(car)
        db.session.commit()
    except exc.SQLAlchemyError as e:
        return jsonify({"err": str(e.orig)})
    return jsonify(car)

@cars_routes.route("/car/<int:id>/edit", methods=["POST"])
@login_required
def car_edit(id: int):
    if not current_user.is_admin:
        return jsonify({"err":"You don't have admin rights."})
    try:
        car = ModelCar.query.get_or_404(id)
        car.brand = request.form.get("brand")
        car.model = request.form.get("model")
        car.year = request.form.get("year")
        car.price = request.form.get("price")
        car.fuel_type = request.form.get("fuel_type")
        car.doors = request.form.get("doors")
        car.description = request.form.get("description")
        # car.img = request.form["img"]
        db.session.commit()
    except exc.SQLAlchemyError as e:
        return jsonify({"err": str(e.orig)})
    return jsonify(car)

@cars_routes.route("/car/<int:id>/delete", methods=["DELETE"])
@login_required
def car_delete(id):
    if not current_user.is_admin:
        return jsonify({"err":"You don't have admin rights."})
    car = ModelCar.query.get_or_404(id)
    try:
        db.session.delete(car)
        db.session.commit()
        return jsonify({"status": "success"})
    except exc.SQLAlchemyError as e:
        return jsonify({"err": str(e.orig)})