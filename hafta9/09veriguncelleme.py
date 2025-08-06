import mysql.connector

try:
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Baris3642.",
        database="pythondersleri"
    )
    
    secilen= mydb.cursor()
    
    sql="UPDATE ogrenciler SET sinif='uni' WHERE ad='Baris Kocyigit'"
    secilen.execute(sql)
    mydb.commit()
    
    print(secilen.rowcount,"Kayıt duzeltıldı.")
    
    secilen.execute("SELECT * FROM ogrenciler")
    myresult= secilen.fetchall()
    for x in myresult:
        print(x)

    
    
    
except Exception as xx:
    print("Veri tabanına baglanırken bır hata olustu",xx)