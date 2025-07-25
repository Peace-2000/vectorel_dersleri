class Ilan:
    def __init__(self,ilan_no=0,a="--"):
        self.ilanNo= ilan_no
        self.Aciklama=a
    def ilanBilgisi(aa):
        return f"\n\nİlan bilgisi:{'='*20}\nİlan no:{aa.ilanNo}\nAciklama:{aa.Aciklama}\n" 
    
ilan1= Ilan(8547)
print(ilan1.ilanBilgisi())
ilan2=Ilan(5214,"Yeni ilan")
print(ilan2.ilanBilgisi())

class EvIlanı(Ilan): #ılan sınıfından mıras aldık 
    def __init__(self,ino=0,ack="",m2_= 0,semt_=""):
        super().__init__(ino,ack)
        self.m2= m2_
        self.semt= semt_

    def ilanBilgisi(aa):
        return f"\n\nEv ilanı bilgisi:{'='*20}\nİlan no:{aa.ilanNo}\nAciklama:{aa.Aciklama}\nMetrekare: {aa.m2},Semt: {aa.semt}" 
    
    
ilan3=EvIlanı(6632,"Acil satılık ev 3+1",120,"Kızılay")
print(ilan3.ilanBilgisi())

class KiralıkEv(EvIlanı):
    def __init__(self, ino=0, ack="", m2_=0, semt_=""):
        super().__init__(ino, ack, m2_, semt_)


ilan4=KiralıkEv()

print(ilan4.ilanBilgisi())
    
class AracIlanı(Ilan):
    def __init__(self, ilan_no=0, a="--"):
        super().__init__(ilan_no, a)
    
ilan5=AracIlanı()
ilan5.motor_hacmi=1000

print(ilan5.ilanBilgisi())
print(ilan5.motor_hacmi)

