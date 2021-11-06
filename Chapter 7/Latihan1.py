try:
    namafile = input("Masukkan nama file : ")
    file = open(namafile, "r")
    print("Isi file", namafile, "adalah :")
    print(file.read())
except FileNotFoundError:
    print("File tidak bisa ditemukan")
except UnicodeDecodeError:
    print("File tidak bisa di buka di terminal")