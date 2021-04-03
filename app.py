from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Create Flask instance
app = Flask(__name__)

# fix the discrepancy between sqlalchemy and heroku side postgres -ql
app.config['SQLALCHEMY_DATABASE_URI'] =os.environ.get('DATABASE_URL').replace("://", "ql://", 1)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Create db object
db = SQLAlchemy(app) # conect app with db
migrate = Migrate(app, db) # handle the migrations for this app

# DB connection
class Capital_city(db.Model):
    __tablename__ = 'country'
    country_code = db.Column(db.String, primary_key=True, nullable=False)
    country_name = db.Column(db.String(100), unique=True, nullable=True)
    capital_city = db.Column(db.String(100), unique=False, nullable=True)
    is_visited = db.Column(db.Boolean, unique=False, default=True)

    def __init__(self, country_code, country_name, capital_city, is_visited):
        self.country_code = country_code
        self.country_name = country_name
        self.capital_city = capital_city
        self.is_visited = is_visited


# Through route we access your app
@app.route('/')
def index():
    return render_template('index.html')

"""
@app.route('/home', methods=['GET', 'POST'], defaults={'name' : 'Faical'})
@app.route('/home/<string:name>', methods=['GET', 'POST'])
def home(name):
    return f'<h1>Welcome {name}!!</h1>'
"""

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        country_code = request.form['country_code']
        if country_code == '':
            return render_template('index.html', message='Please enter country code with ISO 2 digits format!!!')

        # Make lower cases to upper cases
        country_code = country_code.upper()

        if db.session.query(Capital_city).get(country_code):
            CC = db.session.query(Capital_city).get(country_code)

        else:
            return render_template('index.html', message='No matching country code!!!')

        return f"<h1> {country_code}'s country name is" \
               f" {CC.country_name} and" \
               f" it's capital city is {CC.capital_city}!</h1>"


if __name__=='__main__':
    app.debug = True
    app.run()
