def dataStat(x):
    maks = max (x)
    minim = min (x)
    average = sum (x) / len(x)
    
    return (average, maks, minim)

data = [11,15,16,14,17,18]
print("Rata rata, Maks, Min Dari ", data, "Adalah", dataStat(data))
