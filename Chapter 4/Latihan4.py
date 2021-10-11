print("Lama Perjalanan")
def akeb(jarakakeb,kecepatan):
    return (jarakakeb*1000)/(kecepatan*1000/60)
def bkec(jarakbkec,kecepatan1):
    return (jarakbkec*1000)/(kecepatan1*1000/60)
def ttl(total,total1,istirahat):
    return (total+total1+istirahat)
#InputData
jarakakeb= float(input("Berapa jarak dari kota A ke kota B : "))
kecepatan= float(input("Berapa kecepatan rata ratanya : "))
total= round(akeb(jarakakeb,kecepatan))
print("Waktu yang dibuthkan dari kota A ke kota B",total, "Menit")
jarakbkec= float(input("Berapa jarak dari kota B ke kota C :"))
kecepatan1= float(input("Berapa kecepatan rata ratanya : "))
total1= round(bkec(jarakbkec,kecepatan1))
print("Waktu yang dibuthkan dari kota B ke kota C",total1, "Menit")
istirahat= float(input("Berapa lama waktu isirahat : "))
ttlo= round(ttl(total,total1,istirahat))
def jamm(ttlo):
    return ttlo/60
def menitt(jam,ttlo):
    return ttlo-jam*60
jam= round(jamm(ttlo))
menit= menitt(jam,ttlo)
print("Lama Perjalanan adalah", jam, "Jam", menit, "menit")
print("Waktu saat Berangkat")
def jam1(jamjeluar,jam):
    return jamkeluar+jam
def menit1(menitkeluar,menit):
    return menitkeluar+menit
jamkeluar= int(input("Jam : "))
menitkeluar= int(input("Menit : "))
smp= jam1(jamkeluar,jam)
smp1= menit1(menitkeluar,menit)
if smp1<60:
    print("Tiba pukul",smp,":",smp1)
