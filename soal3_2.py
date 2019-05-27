# Soal 3.2 - Dosen & Mahasiswa
#-------------------------------

from pymongo import MongoClient
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# connect to Mongo Client
connection = MongoClient('mongodb://localhost:27017/')

# db = 'Kampus', collection = 'Dosen', 'Mahasiswa'
db = connection['Kampus']
dataDosen = db['Dosen']
dataMahasiswa = db['Mahasiswa']

# take data from 'Dosen'
dataDosen_json = []
dosenList = dataDosen.find()

for item in dosenList:
    asalDosen = item['asal']
    namaDosen = item['nama']
    dosen = "dosen"
    usiaDosen = item['usia']

    dataDosen_dict = {
        "asal" : asalDosen,
        "nama" : namaDosen,
        "status" : dosen,
        "usia" : int(usiaDosen)
    }
    dataDosen_json.append(dataDosen_dict)
# print(dataDosen_json)


# take data from 'Mahasiswa'
dataMahasiswa_json = []
mahasiswaList = dataMahasiswa.find()

for i in mahasiswaList:
    asalMahasiswa = i['asal']
    namaMahasiswa = i['nama']
    mahasiswa = "mahasiswa"
    usiaMahasiswa = i['usia']

    dataMahasiswa_dict = {
        "asal" : asalMahasiswa,
        "nama" : namaMahasiswa,
        "status" : mahasiswa,
        "usia" : int(usiaMahasiswa)
    }
    dataMahasiswa_json.append(dataMahasiswa_dict)
# print(dataMahasiswa_json)


# use Pandas to create DataFrame for both Dosen & Mahasiswa
dfDataDosen = pd.DataFrame(dataDosen_json)
dfDataMahasiswa = pd.DataFrame(dataMahasiswa_json)

print(dfDataDosen)
print('\n')
print(dfDataMahasiswa)

# convert it to array using Numpy in order to plot the graph
namaDosen = np.array(dfDataDosen['nama'])
usiaDosen = np.array(dfDataDosen['usia'])
namaMahasiswa = np.array(dfDataMahasiswa['nama'])
usiaMahasiswa = np.array(dfDataMahasiswa['usia'])

# plotting the graph
plt.bar(namaDosen, usiaDosen, color='blue')
plt.bar(namaMahasiswa, usiaMahasiswa, color='yellow')
plt.title('Usia Warga Kampus')
plt.grid(True)
plt.legend(['Dosen', 'Mahasiswa'])

plt.show()