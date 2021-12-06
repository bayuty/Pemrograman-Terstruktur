file = open('e:\datalatno2.txt', 'r')

dataList = []
data = file.readlines()
for i in range(len(data)):
    pecahData = data[i].split('|')
    dataDict = {'NIM' : pecahData[0],
                'Nama Mhs' : pecahData[1],
                'Alamat' : pecahData[2].replace('\n', ' ')}
    dataList.append(dataDict)

print(dataList)

file.close()