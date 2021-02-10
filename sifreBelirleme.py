import getpass

harf= ["a","b","c","d","e","f","g","h","i","j","j","k","l","m","n","o","p","r","s","t","u","v","y","z"]
rakamlar = ["1","2","3","4","5","6","7","8","9","0"]
karakter = ["*","+","-","_",".","?","/"]  
check=1

while (check):
	sifre = getpass.getpass("\nLutfen  sifre  belirleyin: ")
	checkRakam=0 
	checkKarakter=0
	checkHarf=0
	for i in sifre :
		if i  in rakamlar:
			checkRakam+=1

		if i in karakter:
			checkKarakter+=1

		if i in harf:
			checkHarf+=1

	if len(sifre) > 12 or len(sifre) < 6 :
		print("Uyari!!!\nSifrenizin uzunlugu 6 ile 12 arasinda olmak zorundadir.")

	elif checkRakam < 1:
		print("Uyari!!!\nSifreniz en az bir rakam icermelidir.")

	elif checkKarakter < 1:
		print("Uyari!!!\nSifreniz en az bir karakter icermelidir.")

	elif checkHarf < 1:
		print("Uyari!!!\nSifreniz en az bir harf icermelidir.")

	else:
		check=0
		print("""
			Sifre basariyla olusturuldu!
			Lutfen sifrenizi not aliniz.\n""")

		 

	




				




