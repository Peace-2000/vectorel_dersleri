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
    sqlKomutu="INSERT INTO ogrenciler(tc,ad,sinif) VALUES(%s,%s,%s)"
    degerler=[
        ("13211312","Baris Kocyigit","11C"),
        ("1231123","Fuat Saylan","12b"),
        ("312312","Berk Saylan","11C"),
           ]
    # secilen.execute("CREATE TABLE ogrenciler (tc VARCHAR(11),ad VARCHAR(30),sinif VARCHAR(3) )")
    secilen.executemany(sqlKomutu,degerler)
    mydb.commit()
    print(f"{secilen.rowcount} kayıt eklendi.")
    secilen.execute("SELECT * FROM ogrenciler")
    myresult= secilen.fetchall()
    
    for x in myresult:
        print(x)
      
except Exception as xx:
    print("Veri tabanına baglanırken bır hata olustu",xx)