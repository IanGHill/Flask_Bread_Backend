# Flask_Bread_Backend
A Flask, SQLite, SQLAlchemy Backend for the Breadboss application

python3 -m venv .env
source .env/bin/activate
pip3 install Flask
pip3 install python-dotenv
pip3 install flask-sqlalchemy
pip3 install flask-migrate
mkdir app
touch app/__init__.py
touch app/routes.py
touch .flaskenv
touch breadboss.py
touch config.py
touch app/models.py
flask db init
flask db migrate -m"initial table setup"
flask db upgrade
touch seeds.py
