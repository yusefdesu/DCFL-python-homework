import time
import locale
import random as r
locale.setlocale(locale.LC_ALL, 'turkish')

isim = input("Lütfen isminizi giriniz: ")
baslangic = time.time()
dogru = []
yanlis = []
puan = 0
soriler = ["Dünyanın kaç harikası vardır?  A)15  B)11  C)7  D)2",
           "Albert Einstan yaşasaydı kaç yaşında olurdu?  A)112  B)143  C)30  D)55",
           "Bir üçgenin alanı 30,yarı çapıysa 16 ise diyarbakır hangi diyardadır?  A)Türkiye  B)Amasyasda  C)Bulgur cumhuriyeti  D)Amerika birleşmemiş devletler",
           "Çayın içinde ne vardır?  A)Çay  B)Kahve  C)Haşaş  D)Elma",
           "Bu bilgi yarışması ne zaman kuruldu?  A)M.Ö. 2031  B)M.S. 20020  C)0(yani hiç)  D)-1",
           "Antartika nereye yakındır?  A)Neptün  B)Andromeda  C)Beyaz delik  D)Artika",
           "1 ışık yılı kaç mm dir?  A)9,460800e+18  B)9,460800e+31  C)5dk  D)2",
           "2+2 kaç elma eder?  A)Tam elma  B)Yarım elma  C)Çeyrek elma  D)5 elma",
           "Uranüsün başkenti neresidir?  A)Japonya  B)Dominikler  C)Evim  D) Çekirdeği",
           "Kirpiler nasıl uyurlar?  A)Uçarak  B)Yatarak  C)Kalkarak  D)Nefes almadan",
           "Gaziantep ne zaman savaştan gazi çıkmıştır?  A)1331  B)1597  C)1921  D)11",
           "Damlaya ne olur?  A)Allah bilir  B)Buharlaşır  C)Büzülür  D)Kurur",
           "En temiz böcek hangisidir?  A)Hamam böceği  B)Uğur böceği  C)Kebelek  D)Sivri sinek",
           "Ben nereliyim?  A)Samsun  B)Karadeniz  C)Ordu  D)Rize",
           "Klavyede ne var?  A)Harfler  B)Rakamlar  C)Tuşlar  D)Butonlar",
           "Papatya hangi renkdir?  A)Eflatun  B)Beyaz  C)Siyah  D)Kırmızı",
           "Soru sormaya üşenildiği için bu sana jokerdir 1 doğruya sahip olmak için 'yusef-desu subarashi' yaz.",
           "Şimdi şansını ölçüceğiz (ben,sen,o,biz,siz,onlar) bu kelimelerden sadece biri doğru onu yazarsan puanı kaparsın :D",
           "En iyi çocuk karaktere sahip anime hangisidir????  A)Naruto  B)Kyoukai no kanata  C)SPYxFAMİLY  D)Your lie in April",
           "Canım sıkıldığı için sana puan veriyorum değerini bil 'istemiyorum' yaz :D"]
cevaplar = ["C","B","A","A","C","D","A","D","D","B","C","A","C","B","C","B","yusef-desu subarashi","ben","C","istemiyorum"]

print("Bilgi yarışmamıza hoşgeldin",isim)
for i in range(10):
    sayi = []
    sayi = int(round(r.uniform(0,20)))
    cvp = []
    cvp = str(cevaplar[sayi])
    print(soriler[sayi])
    print("Çözmek için 5 saniyen var cevabını BÜYÜK HARFLE yazmayı unutma yazma yeri geldiğinde yazıp enterla... ")
    time.sleep(5)
    gcvp = input("Cevabın: ")
    if gcvp==cvp:
        print("Tebrikler doğru cevap" , isim , "nasıl bildinki ben bilemezdim :D ")
        dogru.append(gcvp)
        puan=+10
    else :
        print("Hehe yanlış bildin" , isim , "bende böyle tahmin etmiştim :) ")
        yanlis.append(gcvp)
son = time.time()
zaman = round(son-baslangic)
print("Yarışmayı bitirdin",isim,"tebrikler.Yarışmadaki yanlış bildiğin ",len(yanlis),"doğru bildiğin",len(dogru),".Puanın: ",puan,".Tam olarak ",zaman,"saniyede bitirmiş oldun.")
puan = 100
print("Bizi tercih ettiğin için samjkna puan artısı yaptık.Yeni puanın: ",puan)