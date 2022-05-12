import random
dificulty=input("Kolay mod için 'k' , orta mod için 'o' , zor mod için 'z' tuşlayınız. ")
if dificulty=="z":
	hak=1
elif dificulty=="o":
	hak=5
else:
	hak=10
pc=int(random.random()*100)
for i in range(hak):
	gamer=int(input("Yapay zeka 0 ile 100 arası bir sayı tuttu tahmin et: "))
	if gamer==pc:
		print("Aferin kazandın.Tebrikler.")
		break
	elif gamer>pc:
		print("Daha küçük olursa iyi olur...")
	elif gamer<pc:
		print("Daha büyük olursa iyi olur...")
	else:
		print("Bilemedin.Üzgünüm kaybettin...")
print("Yapay zekanın tuttuğu sayı = ",pc)