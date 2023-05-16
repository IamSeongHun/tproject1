from flask import Flask, request
import random
from flask_mysqldb import MySQL

 
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'knu_sw!!'
app.config['MYSQL_DB'] = 'db_sample'
mysql = MySQL(app)
 
@app.route('/')
def index():
    return f'''<!doctype html>
    <html>
        <body>
           <form action="/search" method="post">
            <label for="name">이름:</label>
            <input type="text" id="name" name="name"><br><br>
            
            <input type="submit" value="전송">
        </form>
        </body>
    </html>'''
    # cur = mysql.connection.cursor()
    # cur.execute('''SELECT * FROM classroom''')
    # cur.execute('''SELECT * FROM teaches natural join instructor where name="wu"''')

    # result = cur.fetchall()
    # cur.close()
    # return str(result)
    # return str(random.random())
@app.route('/search', methods=['POST'])
def result():
    name = request.form['name']
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM teaches natural join instructor where name='{name}'")

    result = cur.fetchall()
    cur.close()

    


    # HTML 테이블 생성노노 
    table_html = '<table><tr><th>ID</th><th>과목코드</th><th>sec_id</th><th>semester</th><th>year</th><th>name</th><th>dept_name</th><th>salary</th></tr>'
    for row in result:
        table_html += f'<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[4]}</td><td>{row[5]}</td><td>{row[6]}</td><td>{row[7]}</td></tr>'
    table_html += '</table>'

    # CSS 스타일 추가
    table_html += '''
    <style>
    table {
    font-family: Arial, sans-serif;
    border-collapse: collapse;
    width: 80%;
    }

    td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
    }

    tr:nth-child(even) {
    background-color: #dddddd;
    }
    </style>
    '''

    return table_html

    





# def search(name):
#     cur = mysql.connection.cursor()
#     cur.execute(f"SELECT * FROM teaches natural join instructor where name='{name}'")

#     result = cur.fetchall()
#     cur.close()
#     return str(result)
 
 
app.run(debug=True)