class Musteri:
    def __init__(self,aa,xx,yy,zz=0):
        self.TC=aa
        self.ad=xx
        self.hn=yy
        self.__bakiye=zz
    
    def paraYatir(s,ym,k=10):
        s.__bakiye+=(ym-k)
        # s.hesapBilgisi()
        print(f"Yatırılan miktar({ym}tl) {k}tl kadar komisyon kesildi. \nHesaptaki son bakiye:{s.__bakiye}")
        
        
    def hesapBilgisi(self):
        print(f"\n\nMusteri Hesabı:\nTC:{self.TC}\nAdı:{self.ad}\nBakiye:{self.__bakiye}")
        
musteri1=Musteri(8874,"Mete",5566)
musteri2=Musteri(6658,"Dila",8741,5000)

musteri1.hesapBilgisi()
musteri2.hesapBilgisi()

# musteri2.bakiye=10000000
musteri2.paraYatir(1000)
musteri1.paraYatir(2000,0)
