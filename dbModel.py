from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://dbuser:dbpass@127.0.0.1:3306/dbschema'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Below is a db model for AUTOMATION_TEST_CASE table
class AUTOMATION_TEST_CASE(db.Model):
    __tablename__ = 'AUTOMATION_TEST_CASE'
    TEST_CASE_ID  = db.Column(db.Integer, primary_key=True)
    TEST_RUN_ID = db.Column(db.Integer, nullable=False)
    TEST_CASE_NAME = db.Column(db.String(50), nullable=False)
    PRODUCT = db.Column(db.String(30), nullable=False)
    EXECUTION_TIME = db.Column(db.DateTime, nullable=False)
    RESULT = db.Column(db.String(10), nullable=False)

class AUTOMATION_API_AUTH(db.Model):
    __tablename__ = 'AUTOMATION_API_AUTH'
    API_ID  = db.Column(db.Integer, primary_key=True)
    USERNAME = db.Column(db.String(20), nullable=False, unique=True)
    PASSWORD = db.Column(db.String(30), nullable=False)

class AUTOMATION_HOST_DETAILS(db.Model):
    __tablename__ = 'AUTOMATION_HOST_DETAILS'
    HOST_ID = db.Column(db.Integer, primary_key=True)
    API_ID  = db.Column(db.Integer, ForeignKey('AUTOMATION_API_AUTH.API_ID'), nullable=False)
    HOST_IP = db.Column(db.String(10), nullable=False)
    
# Create the database and tables
with app.app_context():
    db.create_all()