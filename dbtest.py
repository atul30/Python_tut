import MySQLdb

conn = MySQLdb.connect(host = 'localhost', database = 'world', user = 'root', password = 'atul3004')
cursor = conn.cursor()

query = "insert into emptab(eno,ename,sal) values (1004,'Anand',4036)"

try:
	cursor.execute(query)
	conn.commit()
	print("1 row inserted")
except:
	conn.rollback()

cursor.execute('select * from emptab')
rows = cursor.fetchall()
print('total numbers of rows = ',cursor.rowcount)
for row in rows:
	eno = row[0]
	ename = row[1]
	salary = row[2]
	print(f'{eno} {ename} {salary}')

cursor.close()
conn.close()
