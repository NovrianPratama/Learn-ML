var1 = [23, 4, 5, 45, 65, 43, 'Machine Learning', 12.5]

print(var1)
print(var1[1:3])
print(var1[1:10:2])
print(var1[6])
print(var1[6][2]) # mengambil isi list dalam list


## LOOPING list
print("\nLooping List")
var = [23, 4, 5, 45, 65, 43, 2, 12.5]
length = len(var)

for i in range(length -1, -1, -1): # mengubah urutan list dimulai dari akhir
    print(i, var[i])
    
# List Comperenshion
print("\nList Comperenshion")
list1 = []
for i in range(1, 31):
    list1.append(i)
print(list1)

list2 = [val for val in range(1, 50) if val % 2 == 1]  # hasilnya akan ganjil
print(list2)

# ========= LIST Function ========== #
print("\nList Function")
data = [23,42,32,1,3,55,32,12,11,10]
print(f'Sebelum di ubah {data}')
data.pop(2) # untuk menghilangkan value diakhir, parameternya bisa di isi dgn index
print(f'Setelah pop {data}')
del data[0] # digunakan untuk menghapus value dengan index
print(f'Setelah del {data}')

print(data.remove(10)) # mengeluarkan value dengan parameter angka di dalam list
print(f'Setelah remove {data}')

# data.clear() # mengapus value dalam list
# print(f'Setelah clear {data}') 

data [4] = 100 # Udpate data pada list
print(f'Setelah clear {data}')

data.insert(1, 88) # insert data pada list
print(f'Setelah insert {data}')

data2 = [99, 991]
data.append(data2) # append data pada list, menambahkan list diakhir, hasilnya masih dalam list []
print(f'Setelah append {data}')

data.extend(data2) # extend data pada list, fungsi sama dgn append tpi hanya mengambil value saja
print(f'Setelah extend {data}')

# part 2 
print('\nPart 2 ')
list2 = [3, 4, 54,2, 3, 34, 2, 1, 10, 34, 45, 94, 234, 100, 36, 23]
counting = list2.count(2) # Menghitung jumlah value yang berada di list
Max = max(list2)
Min = min(list2)
# list2.sort() # sort dari yang terendah ke terbesar
# list2.sort(reverse=True) # membalikkan angka dengan sort 
# list.reverse(list2) # Akan membalikkan angka tanpa berurutan 
# print(list2) 

print(list2.index(3)) # mencari lokasi index dengan value 3 dalam list
print(list2.index(3, 3)) # mencari lokasi index value 3 tpi dimulai setelah index ke 3


# ========== zip function ========= #
print('\nZIP FUNCTION')
''''
Fungis zip sama seperti range
yaitu menggabungkan dua atau lebih iterable (seperti list, tuple, dll.) 
menjadi pasangan elemen.
'''
zip1 = [34, 4, 2, 12, 4, 5] # angka 5 tidak muncul karena tidak ada pasangannya
zip2 = [34, 4, 5, 65, 3]
zip3 = [23, 1, 5, 34, 6]
length = len(zip2)

for a, b in zip(zip1, zip2):
    print(a,b)
    
for i in range(length): # fungsi zip sama seperti range ini
    print(zip3[i], zip2[i])
    
# ========== CONVERT STRING INTO LIST =========== #
print('\nConvert String into List\n')
data_str = input('Masukkan data: ').title()
list_str = data_str.split()
print(list_str)


list_null = []
for i in range(1, 5):
    input_data = input('Masukkan data baru -'+str(i)+':').title()
    print(input_data)
    list_null.append(input_data)
print(list_null)


