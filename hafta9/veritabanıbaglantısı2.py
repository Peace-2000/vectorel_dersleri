import mysql.connector

try:
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Baris3642."
    )
    print("Baglantı tamam")
    secilen= mydb.cursor()
    secilen.execute("CREATE DATABASE pythondersleri")
    secilen.execute("SHOW DATABASES")
    
    vt_listesi=secilen.fetchall()
    print(*vt_listesi,sep="\n")
except:
    print("Veri tabanına baglanırken bır hata olustu")