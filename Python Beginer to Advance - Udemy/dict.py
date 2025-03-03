data_mhs = {
    'Nama' : "Novrian",
    'NIM' : 12250313668,
    'Jurusan': 'Sistem Informasi',
    'Semester': 6
}

print(data_mhs, type(data_mhs))
print(data_mhs['NIM'])

for i in data_mhs:
    print(i)
    
for i in data_mhs:
    print(i, ':', data_mhs[i])
    
    
# ====== DICT FUNCTION ========= #
print('\nDict Function')
harga = {
    'Buah' : "Durian",
    'Harga' : 25000,
    'Lokasi': 'Pekanbaru',
    'Jumlah': 6
}

print(harga)
print(harga.get('Jumlah')) # mengambil value dari key tertentu

for i in harga.keys(): # mengambil key dalam dictionary
    print(i)
print('\n')
for i in harga.values(): # mengambil value dari key saja 
    print(i)
    
for a, b in harga.items(): # items = mengambil key dan value
    print(a, b)

# del harga['Jumlah'] # menghapus key dan value dengan parameter key
# harga.pop('Buah') # mengeluarkan value diakhir
print(harga)


dict_mhs = dict(nama='Ryan', NIM=1225031233, Jurusan ='Sistem Informasi') # cara membuat dict dengan fungsi dict
print(dict_mhs)
print(dict_mhs['NIM'])
dict_mhs['nama'] = 'Ryan Code' # update data key dictionary
print(dict_mhs)
# dict_mhs.clear() # menghapus dict
print(dict_mhs)




# ============== NESTED DICTIONARY ======== #
print('\nNESTED DICTIONARY')
data_mhs = {
    'mahasiswa1' : {'Nama' : "Novrian", 'NIM' : 12250313668, 'Jurusan': 'Sistem Informasi', 'Semester': 6},
    'mahasiswa2' : {'Nama' : "Ryan", 'NIM' : 12250343438, 'Jurusan': 'Ilmu Informasi', 'Semester': 5},
    'mahasiswa3' : {'Nama' : "Rama", 'NIM' : 12250314548, 'Jurusan': 'Teknik Informatika', 'Semester': 6},
    'mahasiswa4' : {'Nama' : "Dani", 'NIM' : 12250312348, 'Jurusan': 'Sisologi', 'Semester': 6},
    'mahasiswa5' : {'Nama' : "Marco", 'NIM' : 12250354568, 'Jurusan': 'Sistem Informasi', 'Semester': 6}
}

print(data_mhs.keys())

for k, v in data_mhs.items():
    print(k, v['Nama'], v['Jurusan']) # Mengambil value tertentu untuk ditampilkan

print('\n')
data_mhs['mahasiswa5']['Nama'] = 'Roronoa Zoro' # mengganti nama nested dict
for k, v in data_mhs.items():
    print(k, v['Nama'])