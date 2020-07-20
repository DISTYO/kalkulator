import os
os.system('clear')
print '############################'
print 'Author : @Distyo'
print 'Youtube:DG CHANNEL'
print 'Group : HTI GROUP'
print '############################'
print
print '\t>>>>>KALKULATOR<<<<<'
print
print '[1] Pertambahan'
print '[2] Pergurangan'
print '[3] Perkalian'
print '[4] Pembagian'
print '[5] Sisa bagi'
print '[6] Permangkatan'
print
pilih = input('Pilih Menunya : ')

if pilih ==1:
	print
	angka_1 = input('Angka Pertama : ')
	angka_2 = input('Angka Kedua : ')
	total = angka_1 + angka_2
	print
	print 'Hasilnya : ', total
	
elif pilih == 2:
	print
	angka_1 = input('Angka Pertama : ')
	angka_2 = input('Angka Kedua : ')
	total = angka_1 - angka_2
	print
	print 'Hasilnya : ', total
	
elif pilih == 3:
	print
	angka_1 = input('Angka Pertama : ')
	angka_2 = input('Angka Kedua : ')
	total = angka_1 * angka_2
	print
	print 'Hasilnya : ', total
	
elif pilih == 4:
	print
	angka_1 = input('Angka Pertama : ')
	angka_2 = input('Angka Kedua : ')
	total = angka_1 / angka_2
	print
	print 'Hasilnya : ', total
	
elif pilih == 5:
	print
	angka_1 = input('Angka Pertama : ')
	angka_2 = input('Angka Kedua : ')
	total = angka_1 % angka_2
	print
	print 'Hasilnya : ', total
	
elif pilih == 6:
	print
	angka_1 = input('Angka Pertama : ')
	angka_2 = input('Angka Kedua : ')
	total = angka_1 ** angka_2
	print
	print 'Hasilnya : ', total
	
else:
	print
	os.system('figlet Menu Tidak Tersedia cuk !!')
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	