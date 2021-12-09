try:
    from datetime import *
    file = open('e:\dataproject2.txt','r')
    isi = file.readlines()
    cari = input('Masukkan Kode Member\t\t: ')
    
    for i in isi:
        data = i.replace('\n','')
        data = data.split('|')
        if cari in data:
            member = data
            break

    if cari in member:
        indeks = member.index(cari)
        tglpengembalian = datetime.date(datetime.now())
        tglkembali = datetime.strptime(member[indeks+4], '%Y-%m-%d').date()

        print ("="*50)
        print ('Data Peminjaman Buku'.rjust(34))
        print ("="*50)
        print ('Kode Member\t\t\t:', member[indeks])
        print ('Nama Member\t\t\t:', member[indeks+1])
        print ('Judul Buku\t\t\t:', member[indeks+2])
        print ('Tanggal Mulai Pengembalian\t:', member[indeks+3])
        print ('Tanggal Maks Pengembalian\t:', member[indeks+4])
        print ('tanggal Pengembalian\t\t:', str(tglpengembalian))
        terlambat = tglpengembalian - tglkembali
        if int(terlambat.days) < 0:
            print ("Tepat Waktu")
        else:
            terlambat = int(terlambat.days)
            denda = terlambat * 2000
            print ('Terlambat\t\t\t:', str(terlambat),'hari')
            print ('Denda\t\t\t\t: Rp.', denda)

except NameError:
    print('Member tidak ditemukan')