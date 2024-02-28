from flask import Flask,jsonify,render_template
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__,
            static_url_path='', 
            static_folder='../public',
            template_folder='../public')

@app.route("/users")
def get_users():
    conn = psycopg2.connect(database = "postgres", 
                            user = "postgres", 
                            host= 'db',
                            password = "postgres",
                            port = 5432)
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM users;')
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return jsonify(rows)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
  return render_template("index.html")