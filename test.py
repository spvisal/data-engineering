import pyodbc

# Trusted Connection to Named Instance
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=.;DATABASE=sandbox;Trusted_Connection=yes;')

cursor=connection.cursor()
cursor.execute("SELECT @@VERSION as version")

while 1:
    row = cursor.fetchone()
    if not row:
        break
    print(row.version)

cursor.close()
connection.close()