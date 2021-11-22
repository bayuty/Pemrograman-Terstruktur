try:
    n = int(input("Masukkan berapa banyak bilangan yang di masukkan : "))
    bil = []
    
    for i  in range(n):
        angka = int(input("Angka Ke - " + str(i+1) + ": "))
        bil = bil + [angka]
        
    bil.sort (reverse=True)
    print("Angka yang anda masukkan adalah", bil)
    
except ValueError:
    print("Input yang anda masukkan bukan angka")