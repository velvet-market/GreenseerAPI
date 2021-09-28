import mysql.connector
from mysql.connector.constants import ClientFlag

config = {
    'user': 'root',
    'password': '1124',
    'host': '34.69.55.209',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': 'ssl/server-ca.pem',
    'ssl_cert': 'ssl/client-cert.pem',
    'ssl_key': 'ssl/client-key.pem',
     'database':"Recycle"
}

# now we establish our connection
cnxn = mysql.connector.connect(**config) 
mycursor = cnxn.cursor()
#mycursor.execute("CREATE TABLE bin (binID VARCHAR(255), count INT, capacity INT, incorrect INT)")
#mycursor.execute("CREATE TABLE items (time VARCHAR(255), Type VARCHAR(255), bindID VARCHAR(225))")
#mycursor.execute("INSERT INTO bin (binID, count,capacity,incorrect) VALUES (%s, %s,%s,%s)",("0","1","20","0"))
cnxn.commit()

mycursor.execute("SELECT * FROM bin")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
