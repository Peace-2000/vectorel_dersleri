class Ogrenci:
    print("Ogrenci sınıfı calıstı..")
    ad= "----"
    soyad=""
    numara=""
    notOrtalamasi= ""
    disiplinCezasi= 0
    
    def bilgi(self):
        print("------Metod calıstı..")
        print("Metod ile Adı: ",self.ad,"Soyadı: ",self.soyad,"Disiplin cezası: ",self.disiplinCezasi)

    def disiplinCezasiEkle(self,eklenecek):
        self.disiplinCezasi+= eklenecek
        
    
print("Ogrenci ad: ",Ogrenci.ad)
print("Ogrenci disiplin cezası: ",Ogrenci.disiplinCezasi)
ogrenci1=Ogrenci()

ogrenci1.bilgi()
Ogrenci.ad="Ali"
ogrenci1.disiplinCezasiEkle(15)
ogrenci1.bilgi()
print("Sınıf varlıklarını gosterır:", Ogrenci.__dict__)

