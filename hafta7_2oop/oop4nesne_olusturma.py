class Ogrenci:
    print("Ogrenci sınıfı calıstı..")
    ad= "----"
    soyad=""
    numara=""
    notOrtalamasi= ""
    disiplinCezasi= 0
    
    def __init__(self,xx,yy):
        self.ad=xx
        self.soyad=yy
    
    def bilgiYaz(aa):
        print(f"\n\nOgrenci bilgisi:\n{aa.ad} {aa.soyad} {aa.disiplinCezasi}")
        
    def disiplinCezasiVer(s):
        s.disiplinCezasi +=10
    
print("Ogrencı adı: ",Ogrenci.ad) 
ogrenci1=Ogrenci("Mercan","Gul")
ogrenci2=Ogrenci("Arda","Keskin")

ogrenci1.bilgiYaz()
ogrenci2.disiplinCezasiVer()
ogrenci2.bilgiYaz()