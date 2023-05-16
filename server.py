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
    cur.execute(f"SELECT * FROM teaches natural join instructor,department where instructor.dept_name=department.dept_name and name='{name}'")

    result = cur.fetchall()
    cur.close()

    table_html=f'<h1>강사정보</h1><p>이름: {name}</p><p>ID: {result[0][0]} </p><p>학과이름: {result[0][6]} </p><p>학과건물: {result[0][9]}</p>'

    cur2 = mysql.connection.cursor()
    cur2.execute(f"SELECT title,year,semester,teaches.course_id,sec_id FROM (instructor natural join teaches),course where teaches.course_id = course.course_id and name='{name}'")

    result2 = cur2.fetchall()
    cur2.close()


    #HTML 테이블  
    table_html += '<h1>모든 강의 내역</h1><table><tr><th>과목이름(title)</th><th>년도(year)</th><th>학기(semester)</th><th>과목ID(course_id)</th><th>분반번호(sec_id)</th></tr>'
    for row in result2:
        table_html += f'<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td><td>{row[4]}</td></tr>'
    table_html += '</table>'

    #CSS 스타일 추가
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
 
 
# app.run(debug=True)
app.run(host='0.0.0.0', port=9900)