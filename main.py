from fastapi import FastAPI
import databases
from sqlalchemy.orm import sessionmaker
from elasticsearch import Elasticsearch
import sqlite3
from models import posts_table, engine, db_uri
from post.schema import Post

connection = sqlite3.connect('csv.db')
cursor = connection.cursor()

app = FastAPI()
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
database = databases.Database(db_uri)

client = Elasticsearch()


def return_query(some_query):
    response = client.search(
        index="posts",
        body={"from": 0, "size": 20, "query": {"match": {"text": some_query}}}
    )
    a = []
    for hit in response['hits']['hits']:
        a.append(hit['_source']['id'])
    return a


def convert_to_dict(record):
    return {'id': record.id, 'text': record.text, 'created_date': record.created_date, 'rubrics': record.rubrics}


@app.get("/items/")
async def read_item(query: str):
    query = posts_table.select().where(posts_table.c.id.in_(return_query(query))).order_by(posts_table.c.created_date.desc())
    result = await database.fetch_all(query)
    return {'data': list(map(convert_to_dict, result))}


@app.delete("/delete/{id}")
async def delete(id: int):
    es.delete(index='posts', doc_type='items', id=id)
    query = posts_table.delete().where(posts_table.c.id == id)
    return await database.execute(query)
