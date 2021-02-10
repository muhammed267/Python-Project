
#Aritmetik Operatorler:

# +  ----->  toplama
# -  ----->  cıkarma
# *  ----->  carpma
# /  ----->  bolme
# ** ----->  kuvvet
# // ----->  taban bolme  (Sayinin tam kısmını alır noktalı kısmını atar. )
# %  ----->  mod alma (Sayının bölümünden kalanı verir.)

# ======Ornekler======
print( 7*"*","Aritmetik Operatorler",7*"*")
print("Toplama        : ", 25+5)
print("Cıkarma        : ", 25-5)
print("Carpma         : ", 25*5)
print("Str ile carpma : ", 5*"Hello World!")
print("Bolme          : ", 25/5)
print("Kuvvet         : ", 25**5)
print("Taban bolme    : ", 25//5)
print("Taban bolme    : ", 25//2.5)
print("Mod alma       : ", 25%5)
print("Mod alma       : ", 25%3)

"""
 Karsılastirma Operatorleri :

  ==  ----->  Eşitse
  !=  ----->  Esit Degilse
  >   ----->  Buyukse
  <   ----->  Kucukse
  >=  ----->  Buyuk Esitse
  <=  ----->  Kucuk Esitse

"""
# ======Ornek1======
print("\n*******Karsılastirma Operatorleri ************\n")
sayi = int(input("Lutfen 1 ile 100 arasinda bir sayi giriniz: "))
if sayi == 50:
	print("Sayi 50'ye esittir.")

elif sayi > 50:
	print("Sayi 50'den buyuktur. ")

elif sayi < 50:
	print("Sayi 50'den kucuktur. ")

# ======Ornek2======

sayi = int(input("\nLutfen 1 ile 50 arasinda bir sayi giriniz: \n"))
if sayi != 50:
	print("Sayi 50'ye esit degildir .")

elif sayi >= 50:
	print("Sayi 50'ye esit ve buyuktur. ")

elif sayi <= 50:
	print("Sayi 50'ye esit ve kucuktur. ")



















