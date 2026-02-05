<div style="text-align: center;">

# 🚗 McQueens Dealership 🚗

<img src="readme_src/bossman.png" width=300px></img>

#### Angular Frontend with Bootstrap | Python Backend with Flask & SqlAlchemy

</div>


## Setup:

## Backend
Inside ```mc-queens-dealership-be/config.py```:<br>
Set your ```SQLALCHEMY_DATABASE_URI```.<br>
you can use SQLite: ```sqlite:///project.db``` <br>
or MySQL ```mysql+pymysql://user:password@localhost:port/tablename```(in this case create your table manually)
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
In case the API PORT has been changed, inside
```mc-queens-dealership-fe\src\app\api-service.ts```
change ```public api_url = 'http://localhost:5000';```
to desired port ```public api_url = 'http://localhost:666';```
```
cd mc-queens-dealership-fe
npm install
npm start
```
Then visit ```http://localhost:4200/``` on your browser

#### Login credentials created with dummy data.

User: ```user@user``` ``` pass: user```<br>
Admin: ```admin@admin``` ```pass: admin```<br>

When registering inside the app your role defaults as ```User```<br>
To change user privileges to ```Admin```: <br>
Go to your database and change column value ```is_admin``` to ```true``` inside ```Users table```
<div style="text-align: center;">

# 🚗🚗🚗 How does it look? 🚗🚗🚗

</div>

## Home page 🚗
<img src="readme_src/home.png"></img>

## Using filters and sorting results 🚗
<img src="readme_src/home_sort_filter.png"></img>

## Login and register page 🚗
<img src="readme_src/login_register.png"></img>

## If you're logged in you can ❤️ a 🚙 which you can later filter the results by. 🚗
<img src="readme_src/home_user.png"></img>

## Single car view page 🚗
<img src="readme_src/car_view_user.png"></img>

## If you're logged in as the Admin you can also create, edit and delete cars. More buttons! 🚗
<img src="readme_src/home_admin.png"></img>

## Let's create an ad! 🚗
<img src="readme_src/car_add.png"></img>

## There it is! 🚗
<img src="readme_src/car_view_admin.png"></img>

## Hmm, maybe a different picture? 🚗
<img src="readme_src/car_edit.png"></img>

## Everything also looks nice on smol devices :3
<div style="text-align: center;">
<img src="readme_src/mobile_view.png"></img>
</div>

<div style="text-align: center;">

## Thanks for sticking around! Hope you enjoyed the presentation :)

</div>
<div style="text-align: center;">
    <img src="readme_src/95.png" width=100px></img>
    <img src="readme_src/95.png" width=100px></img>
    <img src="readme_src/95.png" width=100px></img>
    <img src="readme_src/95.png" width=100px></img>
    <img src="readme_src/95.png" width=100px></img>
</div>


