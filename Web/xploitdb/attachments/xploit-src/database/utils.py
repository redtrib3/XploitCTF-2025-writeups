from .models import Exploit
from . import db
from sqlalchemy import text

def query_exploits(keyword, by):

    # WET principle: Write Everything Twice.

    if by == 'id':
        if isinstance(keyword, str):
            return None
        query = f"SELECT * FROM exploits WHERE id = {keyword}"
    
    if by == 'date':
        query = f"SELECT * FROM exploits WHERE date = '{keyword}'"

    if by == 'title':
        query = f"SELECT * FROM exploits WHERE title LIKE '%{keyword}%'"


    if by == 'author':
        query = f"SELECT * FROM exploits WHERE author LIKE '%{keyword}%'"


    if by == 'type':
        query = f"SELECT * FROM exploits WHERE type LIKE '%{keyword}%'"

    
    if by == 'platform':
        query = f"SELECT * FROM exploits WHERE platform LIKE '%{keyword}%'"


    res = db.session.execute(text(query))
    rows =  res.fetchall()
    rows = [dict(zip(res.keys(), row)) for row in rows]
    if not rows:
        return None
    return rows


