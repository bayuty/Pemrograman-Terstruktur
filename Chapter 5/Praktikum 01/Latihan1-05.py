kode= input("Masukkan Kode Karyawan : ")
nama= input("Masukkan Nama Karyawan : ")
while(True):
    gol= str(input("Masukkan Golongan : "))
    if (gol=="A") or (gol=="a"):
        gjp= 10000000
        pot= 2.5
    elif (gol=="B") or (gol=="b"):
        gjp= 8500000
        pot= 2.0
    elif (gol=="C") or (gol=="c"):
        gjp= 7000000
        pot= 1.5
    elif (gol=="D") or (gol=="d"):
        gjp= 5500000
        pot= 1.0
    else:
        print("Golongan Tidak Valid")
        continue

    stm = int(input("Masukkan Status (1: Menikah, 2: Belum): "))

    if (stm == 1):
        stts = "Menikah"
        tMenikah = 10 / 100 * gjp
        jAnak = int(input("Masukkan jumlah Anak  : "))
        tAnak = 5 / 100 * gjp
        tAnak = tAnak * jAnak
        break
    elif (stm == 2):
        stts = "Belum Menikah"
        tMenikah = 0
        tAnak = 0
        jAnak = "-"
        break
    else:
        print("Status Menikah Tidak Valid")


gjk= gjp + tMenikah + tAnak
pot2 = pot/100*gjp
gaji= gjk - pot2

print("=====================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("-------------------------------------")
print("Nama Karyawan    : ", nama, " (Kode : ", kode, ")")
print("Golongan         : ", gol)
print("Status Menikah   : ", stts)
print("Jumlah Anak      : ", str(jAnak))
print("-------------------------------------")
print("Gaji Pokok       : Rp.", gjp)
print("Tunjangan Menikah: Rp.", int(tMenikah))
print("Tunjangan Anak   : Rp.", int(tAnak))
print("-------------------------------------")
print("Gaji Kotor       : Rp.", int(gjk))
print("Potongan (" + str(pot) + "%)  : Rp.", int(pot2))
print("-------------------------------------")
print("Gaji Bersih      : Rp.", int(gaji))
print("-------------------------------------")