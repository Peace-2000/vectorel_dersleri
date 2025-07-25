from PyQt6.QtWidgets import *
app= QApplication([])

class Sofra(QMainWindow):
    masa =QWidget()
    sini=QHBoxLayout()
    sini.addWidget(QLabel("Label"))
    sini.addWidget(QLineEdit())
    sini.addWidget(QProgressBar())

    masa.setLayout(sini)
    
    
pencere=QWidget()
pencere.setFixedSize(500,300)
tepsi=QVBoxLayout()
tepsi.addWidget(QLabel("Deneme1"))
tepsi.addWidget(QPushButton("Deneme1"))
pencere.setLayout(tepsi)
pencere.show()

misafir1=Sofra()
misafir2=Sofra()
misafir3=Sofra()

misafir1.show()
misafir2.show()
misafir3.show()


app.exec()