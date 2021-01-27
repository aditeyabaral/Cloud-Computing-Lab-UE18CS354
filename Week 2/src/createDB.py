import pymysql

host = 'aa170lj76b4vrxv.c56j6kn4ugy5.us-east-1.rds.amazonaws.com'
user = 'PES1201800366'
password = 'PES1201800366'

connection = pymysql.connect(host, user, password)
cur = connection.cursor()

cur.execute("CREATE DATABASE ADITEYABARAL")

cur.execute("USE ADITEYABARAL")


query = '''CREATE TABLE New_Users (
Personid INT NOT NULL AUTO_INCREMENT,
username varchar(255),
password varchar(255),
age INT,
mobile_number varchar(10),
PRIMARY KEY (Personid)
);'''

# query = "SELECT * FROM New_Users"

cur.execute(query)