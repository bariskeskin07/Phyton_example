#%% Basics
class Matematik:
    def topla(self,sayi1,sayi2):
        return sayi1 + sayi2
    
    def cikar(self,sayi1,sayi2):
        return sayi1 - sayi2
    
    def carp(self,sayi1,sayi2):
        return sayi1 * sayi2
    
    def bol(self,sayi1,sayi2):
        return sayi1 / sayi2
    
matematik = Matematik()
print("Toplam = " + str(matematik.topla(2,78)))
#  def topla(sayi1,sayi2):
#        return sayi1 + sayi2  
#    def cikar(sayi1,sayi2):
#        return sayi1 - sayi2    
#    def carp(sayi1,sayi2):
#        return sayi1 * sayi2   
#    def bol(sayi1,sayi2):
#        return sayi1 / sayi2 
#matematik = Matematik()print("Toplam = " + str(matematik.topla(2,78)))
# yukaridaki gibi yazarsan hata alirsin class da mutlaka degerlere self ekle
# self:classin referansina karsilik gelir
#matematik = Matematik() ()' in anlami aslında def'lerin ustunde def__init__() 
#diye alt blok calisir.
#biz bu blogu kendimiz yazalım class Matematik: altına hemen sunu yaz
#def__init__(self):
#   print("Calisti") yazdıgında goreceksin
#conturacture (yapici blok) denir bu bloga
#--------------------------------------------------
#class Matematik:
#    def __init__(self,sayi1,sayi2):
#        self.sayi1 = sayi1
#        self.sayi2 = sayi2
#    def topla(self):
#        return self.sayi1 + self.sayi2
#    
#    def cikar(self):
#        return self.sayi1 - self.sayi2
#    
#    def carp(self):
#        return self.sayi1 * self.sayi2
#    
#    def bol(self):
#        return self.sayi1 / self.sayi2
#    
#matematik = Matematik(2,78)
#matematik1 = Matematik(3,76)
#print("Toplam = " + str(matematik1.topla()))
#Boylede yazilabilir...
#%% Property

class Person:
    def __init__(self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        
person1 = Person("Engin","Demirop",33)
print(person1.firstName)
        

class Worker(Person):
    def __init__(self,salary):
        self.salary = salary

class Customer(Person):
    def __init__(self,creditCardNumber):
        self.creditCardNumber = creditCardNumber

ahmet = Worker()
mehmet = Customer()
ali = Person()

#Burada yazılanlar Inheritance (miras almak) örneğidir
#Çalışan ve müşteri classlarını oluşturduk her ikiside insan olduğu için
#Persondan miras alacağı fonksiyonları elde etmek için aynen bu şekilde 
#class tanımlamasının hemen yanına (Person) yazıyoruz
#ahmet. veya mehmet. yazıldığında age ve lastname miras alındığı gözüküyor
#ali. yaz bak farkettiysen person olduğu için miras alacagı bişey yok kendisi zaten miras alınan class

#%% Module


























