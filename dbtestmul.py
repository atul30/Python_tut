import MySQLdb

def insert_rows(eno,ename,sal):
	conn = MySQLdb.connect(host = 'localhost', database = 'world', user = 'root', password = 'atul3004')
	cursor = conn.cursor()

	query = "insert into emptab(eno,ename,sal) values('%d','%s','%f')"

	vals = (eno,ename,sal)

	try :
		cursor.execute(query % vals)
		conn.commit()
		print('1 rows inserted...')

	except Exception as e:
		print(e)
		conn.rollback()

	finally :
		cursor.close()
		conn.close()

def show_rows():
	conn = MySQLdb.connect(host = 'localhost', database = 'world', user = 'root', password = 'atul3004')
	cursor = conn.cursor()

	query = 'select * from emptab'

	try :
		cursor.execute(query)
		try:
			rows = cursor.fetchall()
			print('total number of rows :', cursor.rowcount)
			for row in rows:
				eno = row[0]
				ename = row[1]
				salary = row[2]
				print(f'{eno} {ename} {salary}')


		except Exception as e :
			print(e)

		
	except :
		print("database error")

	finally :
		cursor.close()
		conn.close()

def del_row(eno):
	query = "delete from emptab where eno = %d"
	args = (eno)
	try:
		conn = MySQLdb.connect(host='localhost', database= 'world', user='root', password='atul3004')
		cursor = conn.cursor()
	except Exception as e:
		print(e)
	try:
		cursor.execute(query % args)
		conn.commit()
		print('matching record(s) deleted...')
	except Exception as e:
		print(e)
		conn.rollback()
		

	

n = int(input("how many emp : "))

if n > 0 :
	for i in range(n):
		x = int(input('enter emp number : '))
		y = input('enter emp name : ')
		z = float(input('enter emp salary : '))

		try:
			insert_rows(x,y,z)
		except Exception as e:
			print(e)
		print('-----------------------')

ans = input('Do you want to print all the records :')

if ans.upper() == 'Y':
	show_rows()

d = input('delet a record y/n: ')

if d.upper() == 'Y':
	eno = int(input('Enter the emp number: '))
	del_row(eno)

ans = input('Do you want to print all the records :')

if ans.upper() == 'Y':
	show_rows()

else :
	exit()






