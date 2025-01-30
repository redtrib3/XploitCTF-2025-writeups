from app import app
from app import app
from database import init_db
import os
from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'database/xploitsearch.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
init_db(app)
