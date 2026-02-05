# 🚗 McQueens Dealership 🚗
<img src="readme_src/bossman.png" width=500px></img>

### Angular Frontend | Python Flask & SqlAlchemy Backend

## Setup:

## Backend
Inside ```mc-queens-dealership-be/config.py```:<br>
Set your ```SQLALCHEMY_DATABASE_URI.```<br>
you can use SQLite: ```"sqlite:///project.db"``` <br>
or MySQL(in this case create your table manually) ```mysql+pymysql://user:password@localhost:port/tablename```
```
cd mc-queens-dealership-be
pipenv install
```
Fill tables with users and cars.
```
pipenv run python dummy.py
```
Start backend.
```
pipenv run python app.py
```
You can set the PORT(defaults at 5000) at which the API will run inside ```mc-queens-dealership-be\app.py```:<br>
From ```app.run(debug=True)``` to ```app.run(port=666, debug=True)```
## Frontend:
```
cd mc-queens-dealership-fe
npm install
npm start
```
In case the API PORT has been changed, inside
```mc-queens-dealership-fe\src\app\api-service.ts```
change ```public api_url = 'http://localhost:5000';```
to desired port ```public api_url = 'http://localhost:666';```



