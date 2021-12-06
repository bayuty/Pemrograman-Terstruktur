file = open('e:\datalatno5.txt', 'r')
for i in file:
    pick = i.split('|')
    hasil = int(pick[0]) + int(pick[1])
    print(hasil)

file.close()