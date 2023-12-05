import mysql.connector
conn = mysql.connector.connect(host='localhost' , password= 'Dvg@5321', user='root')

if conn.is_connected():
	print("Connection established...")






