from flask import jsonify, Blueprint, request
from models import Car as ModelCar, db
from sqlalchemy import exc

cars_routes = Blueprint("cars", __name__)

@cars_routes.route("/cars")
def cars():
    return jsonify(ModelCar.query.all())

@cars_routes.route("/car/<int:id>")
def car_detail(id: int):
    return jsonify(ModelCar.query.get_or_404(id))

@cars_routes.route("/car/create", methods=["POST"])
def car_create():
    try:
        car = ModelCar(
            brand = request.form["brand"],
            model = request.form["model"],
            year = request.form["year"],
            price = request.form["price"],
            fuel_type = request.form["fuel_type"],
            doors = request.form["doors"],
            description = request.form["description"],
            # img = request.form["img"]
        )
        db.session.add(car)
        db.session.commit()
    except exc.SQLAlchemyError as e:
        return jsonify({"err": str(e.orig)})
    return jsonify(car)

@cars_routes.route("/car/<int:id>/edit", methods=["POST"])
def car_edit(id: int):
    try:
        car = ModelCar.query.get_or_404(id)
        car.brand = request.form["brand"]
        car.model = request.form["model"]
        car.year = request.form["year"]
        car.price = request.form["price"]
        car.fuel_type = request.form["fuel_type"]
        car.doors = request.form["doors"]
        car.description = request.form["description"]
        # car.img = request.form["img"]
        db.session.commit()
    except exc.SQLAlchemyError as e:
        return jsonify({"err": str(e.orig)})
    return jsonify(car)

@cars_routes.route("/car/<int:id>/delete", methods=["DELETE"])
def car_delete(id):
    car = ModelCar.query.get_or_404(id)
    try:
        db.session.delete(car)
        db.session.commit()
        return jsonify({"status": "success"})
    except exc.SQLAlchemyError as e:
        return jsonify({"err": str(e.orig)})