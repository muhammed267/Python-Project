#Input
isim = input("İsminizi giriniz: ")
print("Hoşgeldiniz" ,isim, "Bey" )

sayi1 = input("Birinci sayiyi giriniz: ")
sayi2 = input("İkinci sayiyi giriniz: ")
print("type of sayi1 : ",type(sayi1))#input herzaman veri tipini str olarak alır.
print("type of sayi2 : ",type(sayi2))
print(sayi1+sayi2)

sayi1 =int(input("Birinci sayiyi giriniz: "))
sayi2 = int(input("İkinci sayiyi giriniz: "))
print("type of sayi1 : ",type(sayi1))
print("type of sayi2 : ",type(sayi2))
print(sayi1+sayi2)

#Hesap Makinesi
print("Hosgeldiniz lütfen islem yapmak istediğiniz iki sayiyi giriniz: ")
num1 = float(input("Ilk sayiyi giriniz: "))
num2 = float(input("Ikinci sayiyi giriniz: "))
print("=====================================")
print("Sayilarin Toplami : ",num1+num2)
print("Sayilarin Cıkarimi: ",num1-num2)
print("Sayilarin Carpimi : ",num1*num2)
print("Sayilarin Bolumu  : ",num1/num2) 
print("=====================================")
