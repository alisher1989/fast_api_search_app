import sqlite3, csv
import datetime


from models import posts_table, engine

connection = sqlite3.connect('csv.db')
cursor = connection.cursor()


with open('/home/alisher/Загрузки/posts.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        ins = posts_table.insert().values(
            text=row[0],
            created_date=datetime.datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S'),
            rubrics=row[2])
        conn = engine.connect()
        conn.execute(ins)


