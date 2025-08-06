import mysql.connector

try:
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234"
    )
    print("Baglantı tamam")
    print(mydb)
except:
    print("Veri tabanına baglanırken bır hata olustu")