print("-------------------------")
print("PROGRAM HITUNG RATA RATA")
print("-------------------------")

bilbul = 0
jmlh = 0
while True:
    try:
        bil= int(input("Masukkan bilangan bulat : "))
        bilbul += bil
        jmlh += 1
        yn = input("Lagi (y/n) : ")
        if yn == "y" or yn == "Y":
            True
        elif yn == "n" or yn == "N":
            avg = bilbul/jmlh
            print("Rata ratanya adalah : ", avg)
            break
        else :
            print("Input yang anda masukkan salah")
    except ValueError:
        print("Input yang anda masukkan bukan bilangan bulat")
    continue