from flask import Flask, request
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'knu_sw!!'
app.config['MYSQL_DB'] = 'db_sample'

mysql = MySQL(app)


@app.route('/')
def index():
    return '''
        <div style="display: flex; justify-content: center;">
            <form action="/search" method="post">
                <select id="name" name="name">
                    <option value="">--찾을 이름을 선택하시오--</option>
                    <option value="Atanassov">Atanassov</option>
                    <option value="Bawa">Bawa</option>
                    <option value="Bietzk">Bietzk</option>
                    <option value="Bondi">Bondi</option>
                    <option value="Bourrier">Bourrier</option>
                    <option value="Choll">Choll</option>
                    <option value="DAgostino">DAgostino</option>
                    <option value="Dale">Dale</option>
                    <option value="Gustafsson">Gustafsson</option>
                    <option value="Jaekel">Jaekel</option>
                    <option value="Kean">Kean</option>
                    <option value="Lembr">Lembr</option>
                    <option value="Lent">Lent</option>
                    <option value="Liley">Liley</option>
                    <option value="Luo">Luo</option>
                    <option value="Mahmoud">Mahmoud</option>
                    <option value="Mingoz">Mingoz</option>
                    <option value="Morris">Morris</option>
                    <option value="Pimenta">Pimenta</option>
                    <option value="Queiroz">Queiroz</option>
                    <option value="Romero">Romero</option>
                    <option value="Sakurai">Sakurai</option>
                    <option value="Sarkar">Sarkar</option>
                    <option value="Shuming">Shuming</option>
                    <option value="Sullivan">Sullivan</option>
                    <option value="Tung">Tung</option>
                    <option value="Ullman">Ullman</option>
                    <option value="Valtchev">Valtchev</option>
                    <option value="Vicentino">Vicentino</option>
                    <option value="Voronina">Voronina</option>
                    <option value="Wieland">Wieland</option>
                </select>
                <input type="submit" value="검색">
            </form>
        </div>
    '''


@app.route('/search', methods=['POST'])
def result():
#강사정보
    name = request.form['name']
    cur = mysql.connection.cursor()
    cur.execute(
        f"SELECT * FROM teaches natural join instructor,department where instructor.dept_name=department.dept_name and name='{name}'")

    result = cur.fetchall()
    cur.close()

    table_html = f'<h1>강사정보</h1><p>이름: {name}</p><p>ID: {result[0][0]} </p><p>학과이름: {result[0][6]} </p><p>학과건물: {result[0][9]}</p>'

#해당 강사의 모든 강의 내역
    cur = mysql.connection.cursor()
    cur.execute(
        f"SELECT title,year,semester,teaches.course_id,sec_id FROM (instructor natural join teaches),course where teaches.course_id = course.course_id and name='{name}'")

    result = cur.fetchall()
    cur.close()

    for row in result:
        table_html += f'<h1>모든 강의 내역</h1><p>과목이름: {row[0]}</p><p>년도: {row[1]} </p><p>학기: {row[2]} </p><p>과목ID: {row[3]}</p><p>분반번호: {row[4]}</p>'

        cur = mysql.connection.cursor()
        cur.execute(
            f"select row_number() over(order by student.id),dept_name,student.id,name from takes join student on takes.id=student.id where year={row[1]} and semester='{row[2]}' and course_id ={row[3]} and sec_id={row[4]}")

        result2 = cur.fetchall()
        cur.close()

        table_html += '<table><tr><th>순번</th><th>소속</th><th>학번</th><th>학생이름</th></tr>'
        for row in result2:
            table_html += f'<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td></tr>'
        table_html += '</table>'

    # table CSS
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



#app.run(debug=True)
app.run(host='0.0.0.0', port=9900)
#app.run(host='0.0.0.0')
#http://59.23.16.137:9900 이 주소로 가야 외부에서 접속 가능.