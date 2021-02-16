
kitapListesi = list()

menu = """
\u27A4  Kitap Ekleme[1]
\u27A4  Kitap Cıkarma[2]
\u27A4  Kitap Listeleme[3]
\u27A4  Cıkıs[4]
"""
def kitapEkle(yeniKitap,liste):
	
	liste += [yeniKitap]
	
	print("{} isimli kitap listeye basariyla eklendi.\n".format(kitapAdi))
	input("Menuye dönmek icin enter tusuna basiniz. ")

def kitapCıkar():
	input("Menuye dönmek icin enter tusuna basiniz. ")
	pass


def kitapListele(kitapListesi):
	j=1
	print()
	print(30*"=")
	
	for i in kitapListesi:
		print("{}.Kitap Ismi =====>   {} ".format(j,i))
		j +=1
	
	print(30*"=")
	input("\nMenuye dönmek icin enter tusuna basiniz. ")

def cıkıs():
	print("Cıkıs yapılıyor...\n")
	quit()

while True:
	print(menu)

	secim = input("Yapmak istediginiz islemi seciniz : ")

	if secim == "1":
		kitapAdi = input("\nEklemek istediginiz kitabin adi : ")
		kitapEkle(kitapAdi,kitapListesi)

	elif secim == "2":
		kitapCıkar()

	elif secim == "3":
		kitapListele(kitapListesi)

	elif secim == "4":
		cıkıs()


