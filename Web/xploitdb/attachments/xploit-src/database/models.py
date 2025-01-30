from . import db


class Exploit(db.Model):
    __tablename__ = 'exploits'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    date = db.Column(db.Date, nullable=False)
    author = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    platform = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Exploit {self.exploit_id} >'

class Secrets(db.Model):
    __tablename__ = 'company_secrets'
    id = db.Column(db.Integer, primary_key=True)
    secret = db.Column(db.String, nullable=False)
