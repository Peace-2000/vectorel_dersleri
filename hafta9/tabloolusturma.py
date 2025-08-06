import mysql.connector

try:
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Baris3642.",
        database="pythondersleri"
    )
    print("Baglantı tamam")
    secilen= mydb.cursor()
    secilen.execute("CREATE TABLE ogrenciler (tc VARCHAR(11),ad VARCHAR(30),sinif VARCHAR(3) )")

except:
    print("Veri tabanına baglanırken bır hata olustu")