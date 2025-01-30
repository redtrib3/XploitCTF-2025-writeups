from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import csv
import os
from dotenv import load_dotenv

load_dotenv()
db = SQLAlchemy()
secret_string = os.getenv('SECRET_STRING')

def init_db(app):
    db.init_app(app)
    with app.app_context():
        from .models import Exploit, Secrets

        db.create_all()

        # initialize values in table
        if not Exploit.query.first():
            print("[+] Inserting init data...")

            with open('./database/exploit.csv', 'r') as f:
                reader = csv.reader(f)
                next(reader)

                for row in reader:
                    exploit = Exploit(
                            id=row[0],  
                            title=row[1],
                            date=datetime.strptime(row[2], '%Y-%m-%d'), 
                            author=row[3],
                            type=row[4],
                            platform=row[5],
                        )

                    db.session.add(exploit)
                db.session.commit()

        if not Secrets.query.first():
            secret = Secrets(
                id=1337,
                secret=secret_string
            )        
            
            db.session.add(secret)
            db.session.commit()

        print("[+] Database Initialized")
