def sum(*angka):
    hasil = 0
    for data in angka:
        hasil += data

    return hasil

def avg(*angka):
    hasil = sum(*angka)
    jumlah = 0
    for data in angka:
        jumlah += 1

    return hasil / jumlah

def maks(*angka):
    maks = angka[0]
    for data in angka:
        if maks < data:
            maks = data

    return maks

def min(*angka):
    min = angka[0]
    for data in angka:
        if min > data:
            min = data

    return min