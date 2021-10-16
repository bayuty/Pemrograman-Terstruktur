print("Hai.. nama saya Mr. Bayu, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!")
from random import randint
bil = randint(0,100)
sc= 100
while True:
    tb= float(input("Tebakan Anda : "))
    sc -= 2
    if (sc<0):
        print ("Score Anda 0, anda tidak dapat bermain lagi")
        break
    elif (bil<tb):
        print("Hehehe… Bilangan tebakan anda terlalu besar")
    elif (bil>tb):
        print("Hehehe… Bilangan tebakan anda terlalu kecil")
    else :
        print("Yeeee… Bilangan tebakan anda BENAR :-)")
        print("Score Anda : ", sc)
        break