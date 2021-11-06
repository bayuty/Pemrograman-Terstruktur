try:
    namafile = input("Masukkan nama file : ")
    file = open(namafile, "r")
    while True:
        file = open(namafile, "a")
        inptdata = input("Data yang akan ditambahkan : ")
        file.write(inptdata)
        file.close()
        yn = input("Mau lagi (y/n) : ")
        if yn == "y" or yn == "Y":
            True
        elif yn == "n" or yn == "N":
            break
        else :
            print("Input yang anda masukkan tidak valid")
            break
except FileNotFoundError:
    print("File tidak bisa ditemukan")
except UnicodeDecodeError:
    print("File tidak bisa di buka di terminal")