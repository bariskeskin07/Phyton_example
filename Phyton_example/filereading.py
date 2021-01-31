# -*- coding: utf-8 -*-

f = open("musteriler.txt")
#print(f.read())
print("********")
print("aa" + str(f.readline()))
for i in f:
    print(i)
f.close()
#eğer dosyayla işin bitttiyse bu fonksiyonu kullanarak kapat yoksa 
#harbiden dosya açık kalıyor



#print(f.readline())



#yukarıdaki printte 10 karakter okumak istiyorsan readin boşluğuna 10 yaz
#open("ogrenciler.txt","w")
#r Read, a append, w write dosya yoksa yenisini oluşturur
#x create dosyayı oluşturur varsa hata verir.
#f.read() 'in olayı oaln tüm veriyi okur 
#f.readline()'in olayı verileri satır satır okur lakin
#f.read() komutu açıkken f.readline() yaparsan okumaz
#çünkü f.read() tüm satırları okur böylece f.readline() için okuyacak satır kalmaz
# üst üste f.readline() yazarsan ilki birinci satırı diğeri ikinci satırı okur öyle gider
#100 lerce müşteri isimlerini satır satır yazdırmak için güzel bi mantık var
#for döngüsüne alıyourz; for l in f:
#                            print(l) yazarsan tüm satırları (Line) ları okur
# l de ordan gelmekte zaten kafan karışmasın l yerine a b c x u felanda koyabilirsin
fileToAppend = open("ogrenciler.txt","a")
fileToAppend.write("\t")
fileToAppend.write("ahmet")

fileToAppend.close()  
#dosya açıp işlemler yapıp kapatma işlemilerinde her zaman dosya açıp sonra kapatmanın arasında işlem yapıyoruz
#fileToAppend.write("\n") bir satır aşşağı yazar
#fileToAppend.write("\t") tab yapar
#%%
import os
#dosyayı silmek için bu komut kullanılır os.remove("musteriler3.txt")
if os.path.exists("ogrenciler2.txt"):
    os.remove("ogrenciler2.txt")
else:
    print("Dosya yok")

os.rmdir("empty")
#os.rmdir("empty") komutu dosya varsa onu siler empty diye bir dosya oluşturdum
#sonra komutu çalıştırdığımda dosyayı sildi




