import os
import psycopg2
from flask import Flask, render_template

app = Flask(__name__)


def get_db_connection():
  conn = psycopg2.connect(host=os.environ['HOST'],
                          database=os.environ['DB'],
                          user=os.environ['DB'],
                          password=os.environ['DB_PASSWORD'])
  return conn


@app.route('/')
def index():
  conn = get_db_connection()
  cur = conn.cursor()
  cur.execute('SELECT * FROM books;')
  books = cur.fetchall()
  cur.close()
  conn.close()
  return render_template('index.html', books=books)

port = os.environ['PORT']
app.run(host='0.0.0.0', port=int(port))
