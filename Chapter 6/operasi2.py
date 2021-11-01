from operation import *

#Soal No 1
print('2 + 4 * 6 - 4 = ', end='')
x = kali(4,6)
y = jumlah(2,x)
z = kurang(y,4)
print(z)

#Soal No 2
print('(4 + 7)*(6 - 9) = ', end='')
x = jumlah(4,7)
y = kurang(6,9)
z = kali(x,y)
print(z)

#Soal No 3
print('(10 + 2)/(7 + 5)/(12 - 34) = ', end='')
x = jumlah(10,2)
y = jumlah(7,5)
z = kurang(12,34)
q = bagi(x,y)
r = bagi(q,z)
print(r)