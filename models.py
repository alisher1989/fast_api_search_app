from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime

db_uri = 'sqlite:///csv.db'
engine = create_engine(db_uri)
metadata = MetaData(engine)
posts_table = Table('posts', metadata,
              Column('id', Integer, primary_key=True),
              Column('text', String),
              Column('created_date', DateTime),
              Column('rubrics', String),
              )
metadata.create_all()






