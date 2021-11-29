mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO',
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print("===================================================================")
print("NIM      NAMA MAHASISWA          TGL LAHIR           TEMPAT LAHIR")
print("-------------------------------------------------------------------")

for i in mhs:
        iList = i.split(':')
        lahir = iList[2].split('-')
        tglLahir = lahir[2] + '/' + lahir[1] + '/' + lahir[0]
        print(iList[0].ljust(8, ' '), iList[1].ljust(23,' '), tglLahir.ljust(19, ' '), iList[3].ljust(12, ' '))

                
print("-------------------------------------------------------------------")