buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

print('===========================================================')
print('Daftar harga buah per/Kg : ')
print(buah)
print('===========================================================')
while True:
    beli = input('Buah yang dibeli : ')
    if beli in buah:
        kg = int(input('Berapa Kg        : '))
        total = kg * buah[beli]
        print('---------------------------')
        print('Total harga      : ', total)
        break   