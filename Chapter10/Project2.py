file = open('e:\datalatno2.txt','a')
while True:
    nim = input('Masukkan NIM   : ')
    nama = input('Masukkan Nama MHS : ')
    alamat = input('Masukkan Alamat: ')

    file.write(nim + '|' + nama + '|' + alamat + '\n')
    inpt = input('Ulangi input lagi? (y/n): ')
    
    if inpt in('y','Y'):
        continue
    elif inpt in('n', 'N'):
        print('Data ditambahkan')
        file.close()
        break
    else:
        print('Input tidak valid')
        continue