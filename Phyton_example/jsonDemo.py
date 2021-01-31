# -*- coding: utf-8 -*-

import json

with open("user.json") as users:
    data = json.load(users)
    
    for x in range(5):
        print(data[x]["username"]) 
        print(data[x]["email"])
        print(data[x]["address"]["street"])
        print(data[x]["username"])
        print(data[x]["address"]["geo"]["lng"])
        
#    print(data)
#json0.py ve bu dosya aslında şunları öğretir
#json denilen bi veri okuma yöntemi vardır
#bu veri okumada jsonplaceholder denilen bi web sitesinde 
#ordaki users verileri user.json diye copy paste yaptık
#sonrasında verileri okumak için ilk önce json okuma mantığı ne
#bunu bilgisayarın anlamasını sağlamak için kütüphane ekledik
#buda json kütüphanesi oluyor
# sonra with open("açılacak dosyanın ismi") as hangi isimde açılmak isteniyorsa 
#o isim yazılıp sonra : koyacan 
#yani şöyle with open("user.json") as anan: mesela
#sonra o açılan dosyanın verilerini data denilen değişkene aktardık
#ardından printledik f5 e basıldığında elimizde tüm veriler gözüktü
#eger ben bu veerilen sadece bi tanesini görmek istiyorsam print([data])
#yazmam gerek. sadece ismini istiyorsan ordaki karşılığı ne geliyorsa onu yazıp
#data[0]["username"] yazman gerek "username": "Bret", şekilde görüldüğü gibi
#bu yazımın aslında anlamı 0. datanın şununcu şeyi nedir diyosun
#print(data[0]["address"]["street"]) data 0 ın şusunun şusuna ulaşmak demek bu
# aslında bildiğin matris aq
#ilk 4 degere ulaşmak için for içinde rasgele bi şey yaz sonra sınırı koy senin
#istediğin tüm print ifadelerin ilk 4 degerini çıkarır
