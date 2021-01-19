# fast_api_search_app
search using elasticsearch FastApi app

интерфейс на эндпоинты : http://localhost:8000/docs

1) https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html по этой ссылке можете скачать установить на свой компьютер Elasticsearch

2) установка elasticsearch на компьютер(Linux):
      1) wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.10.2-linux-x86_64.tar.gz
      2) wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.10.2-linux-x86_64.tar.gz.sha512
      3) shasum -a 512 -c elasticsearch-7.10.2-linux-x86_64.tar.gz.sha512
      4) tar -xzf elasticsearch-7.10.2-linux-x86_64.tar.gz
      5) cd elasticsearch-7.10.2/
      6) bin/elasticsearch
      
3) git clone https://github.com/alisher1989/fast_api_search_app.git 

4) cd fast_api_search_app/

5) virtualenv -p python3.7 venv

6) source venv/bin/activate

7) pip install --upgrade pip

8) pip install -r req.txt

9) python3.7 models.py

10) python3.7 import.py

11) python3.7 add_to_elasticsearch.py

12) uvicorn main:app --reload
