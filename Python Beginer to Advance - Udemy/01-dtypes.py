'''
Tipe data python
1. Type data Mutable
    Tipe data yang mutable adalah tipe data yang bisa diubah (dimodifikasi) setelah objek tersebut dibuat. 
    Dengan kata lain, nilai atau konten dari objek tersebut bisa diubah tanpa membuat objek baru.
Contoh: List, Dictionary (dict), Set

2. Tipe data Immutable
    Tipe data yang immutable adalah tipe data yang tidak dapat diubah setelah objek tersebut dibuat.
ContohInteger (int), Float, String, Tuple 
'''

FirstName = 'Novrian'
LastName = 'Pratama'
print(FirstName + LastName)

# List
MhsB = ['Novrian', 6, 22, 'Sistem Informasi']
print(MhsB, type(MhsB))
MhsB[1] = 7
print(MhsB)
print(MhsB[2])

# Tupple: immutable, tidak bisa diubah isinya menggunakan index
# bisa melihat value dengan index
nilaiUas = (4, 'Ryan', True, 20)
print(nilaiUas, type(nilaiUas))
print(nilaiUas[1])


# DICTIONARY: memanggila value dengan key pada dict
dataDiri = {
    'nama' : 'Novrian Pratama',
    'NIM' : 12250313668,
    'Kelas' : 'B',
    'Jurusan' : 'Sistem Informasi',
    'Semester' : 6
}

print(dataDiri, type(dataDiri))
print(dataDiri['nama'])
dataDiri['Semester'] = 5
print(dataDiri)

# SET : tidak bisa dipanggil menggunakan index
dataset = {'Rumah', 'Mobil', 3, 5, False}
print(dataset, type(dataset))


## ===========================================######

# Operator
print('\nOperator')
a = 12
b = 10

print('a == b',a == b)
print('a != b',a != b)
print('a > b',a > b)
print('a < b',a < b)
print('a >= b',a >= b)
print('a <= b',a <= b)

## ===========================================######

# Logical Operator
print('\nLogical Operator')
a = 12
b = 10

print('AND :',a < b and a < 10)
print('OR :',a < b or a > 10)
print('NOT :',not a > b)

## ===========================================######
# Membership Operator
print('\nMembership Operator')
a = [2,3,5,10]
b = 10
c = 10

print('IN :', b in a)
print('IN :', 20 in a)
print(' NOT IN :', 20 not in a)
print('is :', b is c)
print(' is not :', b is not c)