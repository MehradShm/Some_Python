import mysql.connector

#Connect To DataBase
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="361e361e",
	database="Test"
	)
#Get Cursor
my_cursor = mydb.cursor()

#Create Database
#my_cursor.execute("CREATE DATABASE Test")

#Show DataBase
#my_cursor.execute("SHOW DATABASES")
#for db in my_cursor:
#	print(db[0])

#Create Table
#my_cursor.execute("CREATE TABLE user (user_id INTEGER(7) AUTO_INCREMENT PRIMARY KEY,name varchar(20), family varchar(20), age INTEGER(3))")
#my_cursor.execute("SHOW TABLES")
#for table in my_cursor:
#	print(table[0])

#Insert One Record
#sqlstuff = "INSERT INTO user(name,family,age) VALUES(%s,%s,%s)"
#record1 = ["Ali" , "Alimohamadi" , 20]
#my_cursor.execute(sqlstuff,record1)
#mydb.commit()

#Insert Multiple Records
#sqlstuff = "INSERT INTO user(name,family,age) VALUES(%s,%s,%s)"
#records = [ ("Amir","Sadeghi",21),
#			("Saeed","Ghiasi",21),
#			("Mehrad","Dadar",20), ]

#my_cursor.executemany(sqlstuff,records) 
#mydb.commit()

#Get Data
#my_cursor.execute("SELECT * FROM user")
#Results = my_cursor.fetchall()
#print("ID\tNAME\tFAMILY")
#print("---\t----\t------")
#for result in Results:
#	print(f"{result[0]}\t{result[1]}\t{result[2]}")
	#print(result[0] + "\t%s" %result[1] + "\t%s" %result[2])

#Where Clause
#my_cursor.execute("SELECT * FROM user WHERE age<=20") #String Uses ''
#for results in my_cursor:
#	print(results[1])

#Like And WildCards
#my_cursor.execute("SELECT * FROM user WHERE name LIKE '%m%'") #String Uses ''
#for results in my_cursor:
#	print(results[1])

#And / Or Clause
#my_cursor.execute("SELECT * FROM user WHERE name LIKE '%m%' Or age=20")#And
#for results in my_cursor:
#	print(results[1])

#Updating Records
#my_sql = "UPDATE user SET age = 20 WHERE name = 'Amir'"
#my_cursor.execute(my_sql)
#mydb.commit()

#Limit Results
#my_cursor.execute("SELECT * FROM user Limit 3 OFFSET 1")
#my_cursor.execute("SELECT * FROM user ORDER BY name DESC") #ASC
#results=my_cursor
#for result in results:
#	print (result)

#delete Records
#my_sql = "DELETE FROM user WHERE user_id=1"
#my_cursor.execute(my_sql)
#mydb.commit()

#Delete Tables
#my_cursor.execute("CREATE TABLE incomes(income INTEGER(7),id INTEGER(7) AUTO_INCREMENT PRIMARY KEY)")
my_sql = "DROP TABLE incomes"
my_cursor.execute(my_sql)