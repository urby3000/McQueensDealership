from flask_jwt_extended import JWTManager
from flask import Flask
from models import db, User as ModelUser, Car as ModelCar
from werkzeug.security import generate_password_hash
from users import users_routes
from cars import cars_routes
from likes import likes_routes
from config import config
import json
import shutil

 
#Flask app
app = Flask(__name__)
    #routes
app.register_blueprint(users_routes)
app.register_blueprint(cars_routes)
app.register_blueprint(likes_routes)
    #config
app.config["SQLALCHEMY_DATABASE_URI"] = config["SQLALCHEMY_DATABASE_URI"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config["SQLALCHEMY_TRACK_MODIFICATIONS"]
app.config["SECRET_KEY"] = config["SECRET_KEY"]
app.config["UPLOAD_EXTENSIONS"] = config["UPLOAD_EXTENSIONS"]
app.config["UPLOAD_PATH"] = config["UPLOAD_PATH"]

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = config["SECRET_KEY"]
jwt = JWTManager(app)


#database
db.init_app(app)

#create db 
with app.app_context():
    db.create_all()
    # Fill db 
    with open('dummy_data/dummy.json') as dummy_file:
        file_contents = dummy_file.read()
    parsed_json = json.loads(file_contents)
    for u in parsed_json["users"]:
        hashed_password = generate_password_hash(u["password"], method="pbkdf2:sha256")
        user = ModelUser(email=u["email"], password=hashed_password, is_admin=u["is_admin"])
        db.session.add(user)
        db.session.commit()

    for c in parsed_json["cars"]:
        car = car = ModelCar(
                brand = c["brand"],
                model = c["model"],
                year = c["year"],
                price = c["price"],
                fuel_type = c["fuel_type"],
                doors = c["doors"],
                description = c["description"],
                image_name = c["image_name"]
            )
        db.session.add(car)
        db.session.commit()

#move pictures
for c in parsed_json["cars"]:
    shutil.copy2("dummy_data/image_uploads/"+c["image_name"], "image_uploads/")

