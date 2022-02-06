
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'sakila'

mysql = MySQL(app)

@app.route('/')
def first():
    return render_template('first.html')
@app.route('/second')
def second():
    if request.method == "POST":
        details = request.form
        # database
        employee = details['ui']
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT UID FROM Teacher")
        results = cur.fetchall()
        if(results == employee):
                 return render_template('teacherloged.html')
        else:
            return render_template('teacher.html')


    return render_template('second.html')
@app.route('/teacher', methods=['GET', 'POST'])
def teacher():
    if request.method == "POST":
        details = request.form
        # database
        firstName = details['tfnames']
        lastName = details['tlnames']
        employee = details['tuids']
        password = details['tp']
        subject = details['tsid']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Teacher(FirstName, LastName, UID ,Subject,  Password) VALUES (%s, %s, %s, %s, %s)",
                    (firstName, lastName, employee,subject, password ))
        mysql.connection.commit()
        cur.close()
    return render_template('teacher.html')

@app.route('/teacherloged', methods=['GET', 'POST'])
def teacherloged():
    if request.method == "POST":
        det = request.form
        # database
        subjectname = det['tlfnames']
        mark = det['tllnames']
        attendence = det['tlsuid']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Students(SubjectName, Mark, Attendence) VALUES (%s, %s, %s)", (subjectname, mark, attendence))
        mysql.connection.commit()
        cur.close()
        return render_template('studentlog.html', nid=subjectname, lid=mark, uid=attendence)
    return render_template('teacherloged.html')
@app.route('/st')
def st():
    return render_template('st.html')
@app.route('/studentlog')
def studentlog():
    return render_template('studentlog.html')

if __name__ == "__main__":
    app.run()