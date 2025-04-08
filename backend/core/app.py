import os
from dotenv import load_dotenv
from apiflask import APIFlask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from sqlalchemy.engine import URL

load_dotenv()

ENV = os.getenv('ENV') or 'development'
HOST = os.getenv('HOST') or 'localhost'
PORT = int(os.getenv('PORT') or 5000)
SQL_SERVER_DRIVER = os.getenv('SQL_SERVER_DRIVER')
SQL_SERVER_CONN = URL.create("mssql+pyodbc", query={"odbc_connect": SQL_SERVER_DRIVER})
SQLALCHEMY_BINDS = { 'mssql': SQL_SERVER_CONN }

app = APIFlask(__name__, title='Cinema API', version='0.0.1', enable_openapi=ENV == 'development')
CORS(app)

app.config['JWT_SECRET_KEY'] = 'super-secret987'  # Change this!
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_BINDS'] = SQLALCHEMY_BINDS

db = SQLAlchemy(app)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)
