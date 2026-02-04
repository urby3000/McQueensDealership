config = {
    # "SQLALCHEMY_DATABASE_URI" : "sqlite:///project.db",
    "SQLALCHEMY_DATABASE_URI" : "mysql+pymysql://root:admin@localhost:3306/mc-queens-dealership",
    "SQLALCHEMY_TRACK_MODIFICATIONS" : False,
    "SECRET_KEY" : "supersecretkey",
    "UPLOAD_EXTENSIONS" : [".jpg", ".png"],
    "UPLOAD_PATH" : "image_uploads"
    }