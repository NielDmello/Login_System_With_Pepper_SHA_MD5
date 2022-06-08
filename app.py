from flask import Flask, render_template, request
import os
import pymysql
import hashlib
import hmac
import random
import string

'''mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="",
  database="userloginfinal"
)


mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE users (uname VARCHAR(255), haspass VARCHAR(255), salt VARCHAR(255))")'''

mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="",
  database="userloginfinal"
)

mycursor = mydb.cursor()

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def main():
    return render_template('index.html')

@app.route('/send_data', methods = ['POST'])
def get_data_from_html():
        username = request.form['username']
        password = request.form['password']

        salt=''.join(random.choices(string.ascii_lowercase, k=8))

        peppered_password = hmac.new(salt.encode("utf-8"), password.encode("utf-8"), hashlib.sha256).hexdigest()

        sql = "INSERT INTO users (uname, haspass ,salt) VALUES (%s, %s ,%s)"
        val=(username,peppered_password,salt)

        mycursor.execute(sql, val)


        mydb.commit()
        
        return "Successfully Registered"

@app.route('/send_data1', methods = ['POST'])
def get_data_from_htmll():
        lusername = request.form['lusername']
        lpassword = request.form['lpassword']

        sqla = "SELECT * FROM users WHERE uname = %s"

        usernam = lusername
        mycursor.execute(sqla, usernam)

        myresult = mycursor.fetchall()

        mydb.commit()

        for x in myresult:
          lst=list(x)
          lif1=lst[1]
          lif2=lst[2]
    
          saltn=lif2
          peppered_passwordn = hmac.new(saltn.encode("utf-8"), lpassword.encode("utf-8"), hashlib.sha256).hexdigest()

          
          if peppered_passwordn==lif1:
            return "Login Success"
          else:
            return "Invalid Login "



if __name__ == '__main__':
  port=int(os.environ.get('PORT',5000))
  app.run(port=port,debug=True,use_reloader=False)