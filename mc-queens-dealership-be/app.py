
from flask_login import LoginManager
from flask import Flask, jsonify, request
from models import db, User as ModelUser
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

#login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
# Load user for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return ModelUser.query.get(int(user_id))

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