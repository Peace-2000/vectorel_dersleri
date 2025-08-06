from PyQt6.QtWidgets import *
from mySql import veritabani_baglanti

class StokMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("STOK MODÜLÜ")
        self.setFixedSize(600, 300)

        # Ana layout
        gicerik = QVBoxLayout()

        # Üst başlıklar
        yicerik1 = QHBoxLayout()
        yicerik1.addWidget(QLabel("Ürün Stok No"))
        yicerik1.addWidget(QLabel("Stok Adı"))
        yicerik1.addWidget(QLabel("Stok Miktarı"))

        # Kullanıcıdan alınan veriler
        yicerik2 = QHBoxLayout()
        self.stok_no = QLineEdit()
        self.stok_adi = QLineEdit()
        self.stok_miktari = QLineEdit()
        yicerik2.addWidget(self.stok_no)
        yicerik2.addWidget(self.stok_adi)
        yicerik2.addWidget(self.stok_miktari)

        # Ek bilgiler
        dicerik1 = QVBoxLayout()

        yicerik3 = QHBoxLayout()
        self.stok_mensei = QLineEdit()
        yicerik3.addWidget(QLabel("Stok Menşei:"))
        yicerik3.addWidget(self.stok_mensei)

        yicerik4 = QHBoxLayout()
        self.stok_cinsi = QLineEdit()
        yicerik4.addWidget(QLabel("Stok Cinsi:"))
        yicerik4.addWidget(self.stok_cinsi)

        yicerik5 = QHBoxLayout()
        self.stok_durumu = QLineEdit()
        yicerik5.addWidget(QLabel("Stok Durumu:"))
        yicerik5.addWidget(self.stok_durumu)

        dicerik1.addLayout(yicerik3)
        dicerik1.addLayout(yicerik4)
        dicerik1.addLayout(yicerik5)

        # Düğmeler
        dugmeler = QHBoxLayout()
        btn_kaydet = QPushButton("Kaydet")
        btn_kaydet.clicked.connect(self.kaydet)
        btn_iptal = QPushButton("İptal")
        btn_iptal.clicked.connect(self.temizle)
        btn_cikis = QPushButton("Çıkış")
        btn_cikis.clicked.connect(self.close)

        dugmeler.addWidget(btn_kaydet)
        dugmeler.addWidget(btn_iptal)
        dugmeler.addWidget(btn_cikis)

        # Layoutları birleştir
        gicerik.addLayout(yicerik1)
        gicerik.addLayout(yicerik2)
        gicerik.addLayout(dicerik1)
        gicerik.addLayout(dugmeler)

        # Ana widget
        araclar = QWidget()
        araclar.setLayout(gicerik)
        self.setCentralWidget(araclar)

    def kaydet(self):
        print("🟡 Kaydet fonksiyonu çağrıldı.")
        try:
            stok_no = self.stok_no.text().strip()
            stok_adi = self.stok_adi.text().strip()
            miktar_text = self.stok_miktari.text().strip()
            stok_mensei = self.stok_mensei.text().strip()
            stok_cinsi = self.stok_cinsi.text().strip()
            stok_durumu = self.stok_durumu.text().strip()

            print("📥 Girilen veriler:")
            print(f"Stok No: {stok_no}, Adı: {stok_adi}, Miktar: {miktar_text}")

            if not stok_no or not stok_adi or not miktar_text:
                print("❗ Eksik bilgi tespit edildi.")
                QMessageBox.warning(self, "Eksik Bilgi", "Stok No, Adı ve Miktarı doldurulmalıdır.")
                return

            if not miktar_text.isdigit():
                print("❗ Miktar geçerli değil.")
                QMessageBox.warning(self, "Hatalı Veri", "Stok miktarı sayı olmalıdır.")
                return

            stok_miktari = int(miktar_text)

            conn = veritabani_baglanti()
            if conn is None:
                print("❌ Veritabanı bağlantısı başarısız.")
                QMessageBox.critical(self, "Bağlantı Hatası", "Veritabanı bağlantısı kurulamadı!")
                return

            cursor = conn.cursor()
            cursor.execute("SELECT DATABASE()")
            aktif_db = cursor.fetchone()
            print("📡 Bağlı veritabanı:", aktif_db)

            sql = """
                INSERT INTO stoklar (stok_no, stok_adi, stok_miktari, stok_mensei, stok_cinsi, stok_durumu)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (stok_no, stok_adi, stok_miktari, stok_mensei, stok_cinsi, stok_durumu)
            print("📤 SQL:", sql)
            print("📦 Veriler:", values)

            cursor.execute(sql, values)
            conn.commit()
            conn.close()

            print("✅ Veri başarıyla eklendi.")
            QMessageBox.information(self, "Başarılı", "Kayıt başarıyla eklendi!")
            self.temizle()

        except Exception as e:
            import traceback
            print("❌ HATA:", e)
            print(traceback.format_exc())
            QMessageBox.critical(self, "Hata", f"Kayıt sırasında hata oluştu:\n{e}")

    def temizle(self):
        self.stok_no.clear()
        self.stok_adi.clear()
        self.stok_miktari.clear()
        self.stok_mensei.clear()
        self.stok_cinsi.clear()
        self.stok_durumu.clear()
        print("🔄 Temizleme tamamlandı.")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    pencere = StokMenu()
    pencere.show()
    sys.exit(app.exec())
