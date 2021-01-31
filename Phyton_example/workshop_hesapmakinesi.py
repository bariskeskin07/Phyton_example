# -*- coding: utf-8 -*-
def topla(sayi1,sayi2):
    return sayi1 + sayi2

def cikar(sayi1,sayi2):
    return sayi1 - sayi2

def carp(sayi1,sayi2):
    return sayi1 * sayi2

def bol(sayi1,sayi2):
    return sayi1 / sayi2


print("Operasyon")
print("1 : Topla")
print("2 : Çıkar")
print("3 : Çarp")
print("4 : Böl")

option = input("Operasyon seçiminiz?")

sayi1 = int(input("Birinci sayı?"))
sayi2 = int(input("İkinci sayı?"))

if option == '1':
    print("Toplam : " +str(topla(sayi1,sayi2)))
    
elif option == '2':
    print("Çıkar : " +str(cikar(sayi1,sayi2)))

elif option == '3':
    print("Çarp : " +str(carp(sayi1,sayi2)))

elif option == '4':
    print("Böl : " +str(bol(sayi1,sayi2)))
    
else:
    print("Geçersiz seçenek")    