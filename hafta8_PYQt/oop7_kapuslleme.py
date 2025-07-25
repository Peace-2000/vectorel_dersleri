class Ogrenci:
    def __init__(self,xx,yy,zz="Normal"):
        self._ad=xx #puclic her sınıfa her yere acık
        self.no=yy
        self.__sd=zz #private dışardan ulaşılamayan değişken
        #sadece kendı sınıfının ıcındekı metodlar ıle ulasılabılır
        
    def saglikDurumu(self):
            return self.__sd + "(Ozel Bilgi)"
        
ogrenci1=Ogrenci("Murat",698)
ogrenci2=Ogrenci("Dila",741,"Astımı var") #nesneye veri set etme
    
# print(ogrenci2.__sd)
print(ogrenci1._ad)
print(ogrenci2._ad)
print(ogrenci2.no)
# print(ogrenci1.__sd)
print(ogrenci1.saglikDurumu())
print(ogrenci2.saglikDurumu())