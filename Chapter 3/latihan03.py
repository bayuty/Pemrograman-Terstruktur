print(" ———Rental Mobil Gacongegas———")
def total(harga12jam,perjam):
    """fungsi untuk menghitung Total bayar"""
    return harga12jam+perjam*166
#input data
harga12jam= int(input("Tarif untuk 12 Jam: "))
perjam= int(input("Tambahan waktu dalam menit: "))
Total=total(harga12jam,perjam)
print("Total Harga = ", "Rp.",Total)
Bayar=int(input("Jumlah Nominal Uang =" ))
Kembalian= (Bayar-Total)
print("Uang Kembalian = ", "Rp.",Kembalian)