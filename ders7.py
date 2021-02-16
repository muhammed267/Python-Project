#Listeler

tipler = ["python",25,10.5,["a","b","a"]] # ( ya da liste() )   (" Bir liste birden farkli veri tiplerini tutabilir. ")

for i in tipler:
	print(type(i))

print("\n")
#Listeye eleman ekleme :

Kitaplar = ["Senden Önce Ben", "The Little Prince", "Simyacı"]

for kitap in Kitaplar:
	print("Kitap adi : {} ".format(kitap))

eklenecekKitap = input("\nEklemek istediginiz kitap : ")
Kitaplar += [eklenecekKitap]

for kitap in Kitaplar:
	print("\u27FE  Kitap adi : {} ".format(kitap))

	