file = open('e:\datalatno1.txt', 'r')
genap = 0
ganjil = 0
for i in file:
    if int(i) % 2 == 0:
        genap += 1
    else:
        ganjil += 1


hasil = {'genap' : genap, 'ganjil' : ganjil}
print('Banyaknya bilangan genap  : ', hasil.get('genap'))
print('Banyaknya bilangan ganjil : ', hasil.get('ganjil'))
file.close()