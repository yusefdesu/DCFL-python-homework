import secrets
şifreler=[]

def oluştur():
    sifre_uzunluk  = 16
    sifre=(secrets.token_urlsafe(sifre_uzunluk))
    liste=[]
    liste.append(sifre)
    print(liste)
for i in range(10) :
 şifreler.append(oluştur())