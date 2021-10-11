print(" ———Rental Mobil Gacongegas———")
def Jam(jamkeluar,jamkembali):
    return jamkembali-jamkeluar
def menit(menitkeluar,menitkembali):
    return menitkembali-menitkeluar
def keseluruhan(lamajam,lamamenit):
    return lamajam*60+lamamenit
#inputdata
print("Waktu saat pinjam")
jamkeluar= int(input("Jam : "))
menitkeluar= int(input("Menit : "))
print("Waktu saat kembali")
jamkembali= int(input("Jam : "))
menitkembali= int(input("Menit : "))
lamajam= Jam(jamkeluar,jamkembali)
lamamenit= menit(menitkeluar,menitkembali)
print("Lama Pinjam = ",lamajam, "Jam",lamamenit, "Menit")
total= keseluruhan(lamajam,lamamenit)
if total<721:
    print("Harga = Rp 200.000")
elif total>720:
    Total= int((total-720)*166.6666666666667+200000)
    print("Harga = Rp.", Total)