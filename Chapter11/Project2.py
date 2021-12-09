from datetime import *

file = open("e:\dataproject2.txt", "a") 

while True:
        komem = input('Masukkan Kode Member\t: ')
        nama = input('Masukkan Nama Member\t: ')
        judulbuku = input('Masukkan Judul Buku\t: ')
        tgl = datetime.date(datetime.now())
        tglkembali = tgl + timedelta(days=7)
        data = [komem, nama, judulbuku, str(tgl), str(tglkembali)]
        file.write('|'.join(data) + '\n')
        
        yn = input('Ulangi lagi? (y/n): ')
    
        if yn == 'y':
            continue
        elif yn == 'n':
            print('Data sudah ditambahkan')
            file.close()
            break