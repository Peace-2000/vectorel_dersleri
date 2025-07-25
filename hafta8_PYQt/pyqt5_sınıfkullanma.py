from PyQt6.QtWidgets import *
app= QApplication([])

pencere=QWidget()
pencere.setFixedSize(500,300)
tepsi=QVBoxLayout()
tepsi.addWidget(QLabel("Deneme1"))
tepsi.addWidget(QPushButton("Deneme1"))
pencere.setLayout(tepsi)
pencere.show()

masa =QWidget()

sini=QHBoxLayout()
sini.addWidget(QLabel("Label"))
sini.addWidget(QLineEdit())
sini.addWidget(QProgressBar())

masa.setLayout(sini)
masa.show()

app.exec()