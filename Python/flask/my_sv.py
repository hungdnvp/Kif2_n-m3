from flask import Flask,request,render_template
from flask_cors import CORS,cross_origin
from werkzeug.exceptions import abort
import sqlite3
# connect database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn
# response 
def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',(post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

app = Flask(__name__)

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/',methods =['POST','GET'])
@cross_origin(origin='*')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/add',methods =['POST','GET'])
@cross_origin(origin='*')
def add_process():
    a = int(request.args.get('sothunhat'))
    b = int(request.args.get('sothuhai'))
    return 'ket qua la: ' + str(a+b)

@app.route('/viethoa',methods =['POST','GET'])
@cross_origin(origin='*')
def upper_process():
    s = request.args.get("chuoi")
    return s.upper()
if __name__ == "__main__":
    app.run(host='0.0.0.0',port='6969')