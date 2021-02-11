def sagSlas(adet):
	for i in range(int(adet)):
		print("\\", end = ""  )

def solSlas(adet):
	for i in range(int(adet)):
		print("/", end = "" )

def bosluk(adet):
	for i in range(int(adet)):
		print(" ",end = "")

def altSatir(adet):
	for i in range(int(adet)):
		print()

def ustKisim(cap):

	for i in range(int(cap/2)):
		boslukSayisi = cap/2-1
		bosluk(boslukSayisi-i)
		solSlas(1)
		bosluk(i*2)
		sagSlas(1)
		altSatir(1)

def altKisim(cap):
	
	for i in range(int(cap/2)):
		bosluk(i)
		sagSlas(1)
		bosluk(cap-2*i-2)
		solSlas(1)
		altSatir(1)

def parelelKenar(cap):
	ustKisim(cap)
	altKisim(cap)

uzunluk = input("Birim girin(Cift sayilarda daha iyi sonuc verecektir.): ")

parelelKenar(int(uzunluk))
