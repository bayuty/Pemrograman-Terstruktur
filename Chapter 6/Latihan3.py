#Menghitung Faktorial dengan menggunakan perulangan for
def faktorial(n):
    faktor = 1
    while (n > 0):
        faktor *= n
        n -= 1
    return faktor

#Menghitung Kombinasi
def C(a,b):
    c = faktorial(a) / (faktorial(b) * faktorial(a - b))
    print (c)
        
#Menghitung Permutasi
def P(a,b):
    p = faktorial(a) / faktorial(a-b)
    print (p)

C(5,3)
P(10,7)