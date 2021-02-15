#Kacıs Dizileri

#1 : Alt satira inmek ("\n")

print("Galatasaray\n",end = "")
print("Fenerbahce")
print("Trabzonspor",end = "")#(end = "\n") olarak bulunan end parametresini istedigimiz sekilde degistirebiliyoz.
print("Besiktas\n")

#2 : Bip Sesi ("\a")

print("Bip Sesi!!!")
print("\a")

#5 : Sekme ("\t")  ("Tab sekmesi kadar bosluk birakmak icin kullanilir.")

print("\tGuido\n\tvas\n\tRossum\n")

#4 : Dusey Sekme 

print("Steve\vJobs\n")

#6 : Soldaki karakteri silme ("\b")

print("Tür\bkiye\n")
print("20\b21\n")
print("Bayrak\b \n\n",end = "") #sondaki karakteri silmek icin end parametresini ("") olarak gostermek zorundasiniz.
print("Paulo\b") #Bu sekilde calısmaz.
print("Dybala\n")

#7 : Unicode ("\u")  
"""
'UNICODE, karakterlerin, harflerin, sayıların, ve bilgisayar ekranında gördüğümüz öteki
bütün işaretlerin her biri için tek ve benzersiz bir numaranın tanımlandığı bir sistemdir.
Bu sistemdekod conumu(code point) adı verilen bu numaralar özel bir şekildde gösterilir . '
Örneğin :

ı harfi = u+0131

"""
print("ı harfi : \u0131")

print("\u27FE\n\u2665\n\u272F\n " )

#8 Etkisizlestirme (r)

print("ı harfi :" r"\u0131")




