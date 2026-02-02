from flask_jwt_extended import JWTManager
from flask import Flask
from models import db
from users import users_routes
from cars import cars_routes
from likes import likes_routes

 
#Flask app
app = Flask(__name__)
    #routes
app.register_blueprint(users_routes)
app.register_blueprint(cars_routes)
app.register_blueprint(likes_routes)
    #config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "supersecretkey"

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "supersecretkey"  # Change this!
jwt = JWTManager(app)


#database
db.init_app(app)

#create db
with app.app_context():
    db.create_all()

# @app.route('/')
# def index():
#     return jsonify({'Hello' : 'World!'})

if __name__ == "__main__":
    app.run(debug=True)