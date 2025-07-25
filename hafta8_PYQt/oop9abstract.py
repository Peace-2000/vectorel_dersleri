from abc import ABC, abstractmethod

class Hayvan(ABC):
    def __init__(self):
        print("\nHayvan olustu")
        
    @abstractmethod
    def sesCikar(self):pass
    
    @abstractmethod
    def hareketKabiliyeti(self):pass

class Kus(Hayvan):
    def __init__(self):
        print("\nKus olustu")
        
    def sesCikar(self):
        print("CİK CİK sesi cıkardı")
    
    def hareketKabiliyeti(self):
        print("Kuslar Ucar")

class Ari(Hayvan):
    def sesCikar(self):
        print("Arılar vız vız sesi cıkardı")
    
    def hareketKabiliyeti(self):
        print("Arılar ucar")

h1=Kus()
h1.sesCikar()
h2=Ari()
h2.sesCikar()
h2.hareketKabiliyeti()