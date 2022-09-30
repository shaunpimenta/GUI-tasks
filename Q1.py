import mysql.connector as connector
from mysql.connector import Error

try:
    con = connector.connect(host='localhost', database='testdb', user='root', password='Dipalis123#')
    if con.is_connected():
        db_Info = con.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = con.cursor()
        cursor.execute("show tables;")
        record = cursor.fetchall()
        print("Tables in testdb are: ", record)

        query = "create table user(userid int primary key, username varchar(20), city varchar(20));"
        cursor.execute(query)
        print(" User table created")
        cursor.execute("show tables;")
        record = cursor.fetchall()
        print("Tables in testdb are: ", record)
        cursor.close()
        con.close()
        print("MySQL connection is closed")

        uid = int(input("enter user id :"))
        uname = input("enter user name : ")
        city = input ("enter city : ")
        query = "insert into user values({} ,'{}','{}')".format(uid,uname,city)
        cursor.execute(query)
        query = "select * from user;"
        cursor.execute(query)
        record = cursor.fetchall()
        print("Data in user table : ", record)

except Error as e:
    print("Error while connecting to MySQL", e)