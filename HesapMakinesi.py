#Hesap Makinesi
print("***************Hosgeldiniz**************")
print("""
[1]-Toplama Islemi
[2]-Cıkarma Islemi
[3]-Carpma Islemi 
[4]-Bolme Islemi
[5]-Us Alma Islemi
[6]-Cıkıs

	""")

secim = int(input("Yapmak istediginiz islem: "))

if secim == 1:
   
	sayi1 = float(input("Ilk sayiyi giriniz: "))
	sayi2 = float(input("Ikinci sayiyi giriniz: "))
    

	print("Sayilarin Toplami : ",sayi1+sayi2)

elif secim == 2:
	num1 = float(input("Ilk sayiyi giriniz: "))
	num2 = float(input("Ikinci sayiyi giriniz: "))

	print("Sayilarin Cıkarimi : ",num1-num2)

elif secim == 3:
	num1 = float(input("Ilk sayiyi giriniz: "))
	num2 = float(input("Ikinci sayiyi giriniz: "))

	print("Sayilarin Carpimi: ",num1*num2)

elif secim == 4:
	num1 = float(input("Ilk sayiyi giriniz: "))
	num2 = float(input("Ikinci sayiyi giriniz: "))

	print("Sayilarin Bolumu : ",num1/num2)

elif secim == 5:
	num1 = float(input("Taban giriniz: "))
	num2 = float(input("Kuvvet giriniz: "))

	print("Us Alma Sonucu: ",num1**num2)

elif secim == 6:
	print("Cıkıs Yapiliyor....")
else:
	print("Yanlıs deger girildi.")




#print("Lütfen islem yapmak istediğiniz iki sayiyi giriniz: ")
#num1 = float(input("Ilk sayiyi giriniz: "))
#num2 = float(input("Ikinci sayiyi giriniz: "))
#print("=====================================")
#print("Sayilarin Toplami : ",num1+num2)
#print("Sayilarin Cıkarimi: ",num1-num2)
#print("Sayilarin Carpimi : ",num1*num2)
#print("Sayilarin Bolumu  : ",num1/num2) 
#print("=====================================")

