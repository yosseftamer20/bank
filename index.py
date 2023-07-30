from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = '123'


def handle_db(sql):
    conn = sqlite3.connect(r'C:\Users\yosse\PycharmProjects\pythonProject1\bank_system\bank_db.sqlite')
    cursor = conn.cursor()
    cursor.execute(sql)
    if sql.lower().startswith('select'):
        col_names = [i[0] for i in cursor.description]
        result = cursor.fetchall()
        return {"headers":col_names, "result":result}
    else:
        conn.commit()
    cursor.close()
    conn.close()


@app.route('/')
def start():
    if not session:
        if request.args:
            email = request.args["email"]
            password = request.args["password"]
            sql = f"select id,name,email,password,type from main.users where email='{email}' and password='{password}'"
            login = handle_db(sql)
            if login:
                session['id'] = login['result'][0][0]
                session['name'] = login['result'][0][1]
                session['email'] = login['result'][0][2]
                session['type'] = login['result'][0][4]
                if login['result'][0][4] == 'admin':
                    return render_template('admins.html', x=session['name'])
                else:
                    return render_template('users.html', x=session['name'])
        else:
            return render_template('log.html')
    else:
        if session['type'] == 'user':
            return render_template('users.html', x=session['name'])
        else:
            return render_template('admin.html', x=session['name'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/create_account')
def create_account():
    if request.args:
        name = request.args['name']
        dob = request.args['dob']
        email = request.args['email']
        password = request.args['password']
        next_id = f"select max(id)+1 from users"
        next_id = next_id[0][0]
        sql = f"insert into users (id, name ,dob,email,password) values ({next_id},'{name}','{dob}','{email}','{password}')"
        handle_db(sql)
        return render_template('users.html')
    else:
        return render_template('create_account.html')


@app.route('/inquery')
def inquery():
    if session['type'] == 'admin':
        data = handle_db(f"select * from users  ")
        return render_template('inquery.html', results=data, x=session['name'])
    else:
        data = handle_db(f"select * from users where id='{session['id']}' ")
        return render_template('inquery.html', results=data, x=session['name'])



@app.route('/deposit')
def deposit():
    if request.args:
        amount = request.args['amount']
        handle_db(f"update users set balance= balance + '{amount}' where id={session['id']}")
        return redirect('/')
    else:
        return render_template('amount.html')

@app.route('/withdraw')
def withdraw():
    if request.args:
        amount = int(request.args['amount'])
        balance = handle_db(f"select * from users where id='{session['id']}'")
        balance=balance['result'][0][6]
        if amount <= balance:
            handle_db(f"update users set balance= balance - '{amount}' where id={session['id']}")
            return redirect('/')
        else:
            return render_template('amount.html', results='The amount is insufficient')
    else:
        return render_template('amount.html')

@app.route('/transfer')
def transfer():
    if request.args:
        email = request.args['email']
        amount = int(request.args['amount'])
        balance1 = handle_db(f"select * from users where id='{session['id']}'")
        balance1 = balance1['result'][0][6]
        balance2 = handle_db(f"select * from users where email='{email}'")
        balance2 = balance2['result'][0][6]

        if amount <= balance1:
            handle_db(f"update users set balance= balance - '{amount}' where id={session['id']}")
            handle_db(f"update users set balance= balance + '{amount}' where email='{email}'")
            return redirect('/')
        else:
            return render_template('amount.html', results='The amount is insufficient', y=True)
    else:
        return render_template('amount.html', y=True)

if __name__ == '__main__':
    app.run(port=80,host='192.168.1.6')
