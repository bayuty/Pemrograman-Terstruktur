print("Konsumsi BBM")
def bbm(jaraktempuh,konsumsibbm):
    return jaraktempuh/konsumsibbm
#InputData
jaraktempuh= float(input("Jarak yang di tempuh : "))
konsumsibbm= float(input("Rata rata konsumsi BBM perliter : "))
Total= bbm(jaraktempuh,konsumsibbm)
print("Jadi, bensin yang dibutuhkan untuk perjalanan adalah sebanyak", Total, "Liter")