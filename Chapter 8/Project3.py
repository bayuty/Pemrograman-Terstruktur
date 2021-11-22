try:
    listnama = []
    while True:
        nama = input("Masukkan Nama : ")
        listnama.append(nama)
        yn = input("Mau lagi (y/n) : ")
        if yn == "y" or yn == "Y":
            True
        elif yn == "n" or yn == "N":
            listnama.sort()
            for nama in listnama :
                print(nama, "(", len(nama), "Karakter )")
            break
        else :
            print("Input yang anda masukkan tidak valid")
            break

except ValueError:
    print("Input yang anda masukkan bukan angka")