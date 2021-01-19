from elasticsearch import Elasticsearch
from sqlalchemy.orm import sessionmaker
from models import engine, posts_table

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
posts = session.query(posts_table).order_by(posts_table.c.created_date.desc()).all()

for i in posts:
    es.index(index='posts', doc_type='items', id=i.id, body={'text': i.text, 'id': i.id})




