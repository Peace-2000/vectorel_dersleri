from PyQt6.QtWidgets import *
aa=QApplication([])

ww=QWidget()
ww.setFixedSize(300,500)
# ww.windowTitle("sss")

icerik=QVBoxLayout()

icerik.addWidget(QPushButton("Tıkla"))
icerik.addWidget(QPushButton("Dene"))
icerik.addWidget(QLabel("Bilgi"))

ww.setLayout(icerik)
ww.show()
aa.exec()