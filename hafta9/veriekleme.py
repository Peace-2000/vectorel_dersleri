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
    degerler=('13211312','Baris Kocyigit','11A')
    # secilen.execute("CREATE TABLE ogrenciler (tc VARCHAR(11),ad VARCHAR(30),sinif VARCHAR(3) )")
    secilen.execute(sqlKomutu,degerler)
    mydb.commit()
    print("1 kayıt eklendı, ID: ",secilen.lastrowid)
    
except Exception as xx:
    print("Veri tabanına baglanırken bır hata olustu",xx)