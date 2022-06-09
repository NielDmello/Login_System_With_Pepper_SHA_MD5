# Login_System_With_Pepper_SHA_MD5
A pepper is similar in concept to a salt or an encryption key. It is like a salt in that it is a randomized value that is added to a password hash, and it is similar to an encryption key in that it should be kept secret


Steps to run the project

install all python packages

pip install flask
pip install os
pip install pymysql
pip install hashlib
pip install hmac
pip install string
pip install random

install xampp for database phpmyadmin

create database userlogin

creater table in database users

mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="",
  database="userlogin"
)


mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE users (uname VARCHAR(255), haspass VARCHAR(255), salt VARCHAR(255))")

save index.html in templates folder

start php server and database

run app.py

type http://127.0.0.1:5000/ in your browser

first register and then login

