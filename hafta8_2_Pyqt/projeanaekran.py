from PyQt6.QtWidgets import *

class StokMenusu(QMainWindow):
    
    def __init__(self,baslik="Uygulama penceresi",e=500,b=300,rr="Cevir"):
        super().__init__()
        self.setWindowTitle("STOK MODULU")
        icerik.addWidget(QLineEdit())
        icerik.addWidget(QLabel("Sonuç: "))


        self.setFixedSize(500,300)

        icerik = QHBoxLayout()
        icerik.addWidget(QLabel("STOK MODULU "))
       
        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)
    
    def dugmeBasma(self):
        print(self.baslikkk," baslıklı pencerede dugmeye bastın")



class AnaMenu(QMainWindow):

    def __init__(self,baslik="Uygulama penceresi",e=500,b=300,rr="Cevir"):
        super().__init__()
        self.setWindowTitle(baslik)
        # self.setFixedSize(e,b)
        self.baslikkk= baslik

        icerik = QVBoxLayout()
        icerik.addWidget(QLabel("Ana Menu"))
        
        dugme1=QPushButton("Stok Modulu")
        dugme1.clicked.connect(self.dugme1Basma)
        icerik.addWidget(dugme1)
        
        dugme2=QPushButton("Fatura Modulu")
        dugme2.clicked.connect(self.dugme2Basma)
        icerik.addWidget(dugme2)
        
        dugme3=QPushButton("Cari Modulu")
        dugme3.clicked.connect(self.dugme3Basma)
        icerik.addWidget(dugme3)
        
        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)
    
    def dugme1Basma(self):
        print("Dugme 1 basıldı")

    def dugme2Basma(self):
        print("Dugme 2 basıldı")

    def dugme3Basma(self):
        print("Dugme 3 basıldı")

    
uygulama = QApplication([])

pencere = AnaMenu("Program Ana Menusu")
pencere.show()



uygulama.exec() 
