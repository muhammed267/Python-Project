#Format Metodu :

print("""
	English : 'Hello World'
	Turkce  : '{}' '{}'
	Русский : '{}'

	""".format("Merhaba","Dunya","Привет мир"))

#Format Bicimleri :

#1 : Konumlandirma 
string1 = "Hello"
string2 = "World"

print("Sola Yatirma : |{:<10}| |{:<10}|".format(string1,string2))
print("Saga Yatirma : |{:>10}| |{:>10}|".format(string1,string2))
print("Merkez       : |{:^10}| |{:^10}| \n".format(string1,string2))

#2 : Sira Belirleme 

kelime1 = "Birinci"
kelime2 = "Ikinci"

print("Sirasiyla        : {}  {}".format(string1,string2))
print("Ters olarak      : {}  {}".format(string2,string1))
print("Konum belirterek : {1} {0}".format(string1,string2))
print("Konum belirterek : {0} {1} \n".format(string1,string2))

#3 : Isim Verme

print("Isim vererek : {ad} {soyad}".format(soyad = "Smith",ad = "Will"	))  #Sira ile yazmak zorunda degiliz.

#4 : Tip Zorunlulugu

print("String zorunlulugu : {:s}".format("Python"))
print("Sayi zorunlulugu   : {:d} \n".format(2021))

#5 : ASCII Tablosundaki Karsiliklari

print("ASCII tablosundaki karsiligi : {:c}".format(75))

A_Harfi= ("ASCII tablosunda 65'in karsılıgı ---> {:c} \n".format(65))
print(A_Harfi)

#6 : Ikılik Sistem

iklikSistem = "30 sayisinin ikilik sistemdeki karsiligi    : {:b}".format(30)
print(iklikSistem)

#7 : Sekizlik Sistem 

sekizlikSistem = "100 sayisinin sekizlik sistemdeki karsiligi : {:o}".format(100)
print(sekizlikSistem)

#8 : Onaltilik Sistem

onaltilikSistem = "150 sayisinin onaltilik sistemde karsiligi : {:x} \n".format(150)
print(sekizlikSistem)

#9 : Sayilari Basamaklarina Ayirma

sayi = "123456789 sayisini basamaklarina ayirma : {:,}".format(123456789)
print(sayi)