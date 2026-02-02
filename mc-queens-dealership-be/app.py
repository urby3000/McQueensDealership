
from flask import Flask, jsonify, request
from models import db
from users import users_routes
from cars import cars_routes
from likes import likes_routes

 
app = Flask(__name__)
app.register_blueprint(users_routes)
app.register_blueprint(cars_routes)
app.register_blueprint(likes_routes)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

# with app.app_context():
#     db.create_all()

@app.route('/')
def index():
    return jsonify({'Hello' : 'World!'})

app.run()