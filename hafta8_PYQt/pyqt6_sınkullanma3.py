from PyQt6.QtWidgets import *

class ceviriPenceresi(QMainWindow):

    def __init__(self,baslik="Uygulama penceresi",e=300,b=300,rr="Cevir"):
        super().__init__()
        self.setWindowTitle(baslik)
        self.setFixedSize(e,b)
        self.baslikkk= baslik

        icerik = QVBoxLayout()
          #icerik = QHBoxLayout()
        icerik.addWidget(QLabel("Çevrilecek: "))
        icerik.addWidget(QLineEdit())
        dugme=QPushButton(rr)
        dugme.clicked.connect(self.dugmeBasma)
        icerik.addWidget(dugme)
        icerik.addWidget(QLabel("Sonuç: "))
        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)
    
    def dugmeBasma(self):
        print(self.baslikkk," baslıklı pencerede dugmeye bastın")

uygulama = QApplication([])

pencere = ceviriPenceresi("444")
pencere.show()


pp=ceviriPenceresi("ee",rr="xxxx")
pp.show()

pp1=ceviriPenceresi("Ceviri ekranı",500,300,"Donustur")
pp1.show()


uygulama.exec() 
