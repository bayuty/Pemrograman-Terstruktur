from datetime import *

def diffdate(x):
    waktu = datetime.strptime(x, '%Y-%m-%d').date()
    waktuskrg = datetime.date(datetime.now())
    selisih =  waktuskrg - waktu
    return selisih
y = "2021-12-1"
print ("Selisih tanggal", y, "dengan hari ini adalah",diffdate('2021-12-1').days)