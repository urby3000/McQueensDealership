from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask import jsonify, Blueprint, request
from models import User as ModelUser, Car as ModelCar, db
from sqlalchemy import exc, asc, desc
from config import config

import os
import uuid
from flask import request, session, send_from_directory
from werkzeug.utils import secure_filename

cars_routes = Blueprint("cars", __name__)

@cars_routes.route('/image_uploads/<filename>')
def get_image(filename):
    return send_from_directory(config['UPLOAD_PATH'], filename)

@cars_routes.route("/cars")
def cars():
    query = db.session.query(ModelCar)
    #sorts ?? xd
    if request.args.get("sortpriceasc"): query = query.order_by(asc(ModelCar.price))
    if request.args.get("sortpricedesc"): query = query.order_by(desc(ModelCar.price))
    if request.args.get("sortbrandasc"): query = query.order_by(ModelCar.brand.asc())
    if request.args.get("sortbranddesc"): query = query.order_by(ModelCar.brand.desc())
    if request.args.get("sortyearasc"): query = query.order_by(ModelCar.year.asc())
    if request.args.get("sortyeardesc"): query = query.order_by(ModelCar.year.desc())

    # #filters 
    if request.args.get("min_price"): query = query.filter(ModelCar.price>=int(request.args.get("min_price")))
    if request.args.get("max_price"): query = query.filter(ModelCar.price<=int(request.args.get("max_price")))

    # ?brand=toyota&brand=bmw
    if request.args.get("brand"): query = query.filter(ModelCar.brand.in_(request.args.getlist("brand")))

    # pagination?!? idk 
    page = request.args.get('page', 1, type=int)  # page number, default 1
    per_page = request.args.get('per-page', 24, type=int)  # cars per page

    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    results = {
        "results": [{"brand": c.brand, 
                     "model": c.model,
                     "price": c.price,
                     "year": c.year,
                     "fuel_type": c.fuel_type,
                     "doors": c.doors,
                     "description": c.description,
                     "image_name": c.image_name,
                     "likes": c.likes,
                     } for c in pagination.items],
        "pagination": {
            "count": pagination.total,
            "page": page,
            "per_page": per_page,
            "pages": pagination.pages,
        },
    }
    return jsonify(results)

@cars_routes.route("/car/<int:id>")
def car_detail(id: int):
    return jsonify(ModelCar.query.get_or_404(id))

@cars_routes.route("/car/create", methods=["POST"])
@jwt_required()
def car_create():
    current_user = ModelUser.query.filter_by(email=get_jwt_identity()).first()
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
            description = request.form.get("description")
        )
        if image_upload(request, car):
            car.image_name = request.files['image_name'].filename
        db.session.add(car)
        db.session.commit()
    except exc.SQLAlchemyError as e:
        return jsonify({"err": str(e.orig)})
    return jsonify({"status": "success"})

@cars_routes.route("/car/<int:id>/edit", methods=["POST"])
@jwt_required()
def car_edit(id: int):
    current_user = ModelUser.query.filter_by(email=get_jwt_identity()).first()
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
        if image_upload(request, car):
            car.image_name = request.files['image_name'].filename
        db.session.commit()
    except exc.SQLAlchemyError as e:
        return jsonify({"err": str(e.orig)})
    return jsonify({"status": "success"})

@cars_routes.route("/car/<int:id>/delete", methods=["DELETE"])
@jwt_required()
def car_delete(id):
    current_user = ModelUser.query.filter_by(email=get_jwt_identity()).first()
    if not current_user.is_admin:
        return jsonify({"err":"You don't have admin rights."})
    car = ModelCar.query.get_or_404(id)
    try:
        db.session.delete(car)
        db.session.commit()
        return jsonify({"status": "success"})
    except exc.SQLAlchemyError as e:
        return jsonify({"err": str(e.orig)})

def image_upload(request, car):
        image = request.files['image_name']

        # check if filepath already exists. append random string if it does
        if secure_filename(image.filename) in [
            img.image_name for img in ModelCar.query.all()
        ]:
            unique_str = str(uuid.uuid4())[:8]
            image.filename = f"{unique_str}_{image.filename}"


        #  handling file uploads
        filename = secure_filename(image.filename)
        if filename:
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in config[
                "UPLOAD_EXTENSIONS"
            ]:
                return {"error": "File type not supported"}, 400

            image.save(os.path.join(config["UPLOAD_PATH"], filename))
            #   removes old image
            if car.image_name and os.path.isfile(os.path.join(config["UPLOAD_PATH"], car.image_name)):
                os.remove(os.path.join(config["UPLOAD_PATH"], car.image_name))
            return True