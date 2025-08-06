import mysql.connector

def veritabani_baglanti():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Baris3642.",
            database="testdb"
        )
        print("🔌 Veritabanı bağlantısı başarılı.")
        return conn
    except mysql.connector.Error as err:
        print(f"❌ Veritabanı bağlantı hatası: {err}")
        return None

if __name__ == "__main__":
    conn = veritabani_baglanti()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS stoklar (
            id INT AUTO_INCREMENT PRIMARY KEY,
            stok_no VARCHAR(100),
            stok_adi VARCHAR(255),
            stok_miktari INT,
            stok_mensei VARCHAR(255),
            stok_cinsi VARCHAR(255),
            stok_durumu VARCHAR(255)
        )
        """)
        conn.commit()
        cursor.close()
        conn.close()
        print("🟢 Tablo başarıyla oluşturuldu.")
