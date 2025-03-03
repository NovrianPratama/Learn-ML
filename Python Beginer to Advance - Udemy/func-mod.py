# FUNCTION METHOD
'''
def sentMsg(nama):
    print('Hello', nama)
sentMsg('Novri') = jika di function ada parameter harus dimasukkan 

def sentMsg():
    print('Hello Novri')
sentMsg() = jika tidak ada bisa dikosongkan

def sentMsg(nama='Novri):
    print('Hello', nama)
sentMsg() = jika kosong maka default outputnya Novri
'''


def sentMsg(nama = 'Novri', bahasa = 'Python'):
    print('Hello', nama)
    print('Saya sedang belajar Pemrograman ', bahasa)
    print('Di Udemy')
    print("")
    
sentMsg('Novri')
sentMsg()
sentMsg('',)
sentMsg('Rama', 'Java')

## RETURN
'''
def sum(a, b):
    hasil = a + b
    print(hasil)
sum(2, b) # jika menggunakan print maka otomatis akan ada hasil

def sum(a, b):
    hasil = a + b
    return hasil # return hasil menyimpan hasil tapi tidak menampilkannya
result = sum(a, b) # simpan dalam variabel baru dan di print kemudian
print(result)
'''

def sum(a, b):
    hasil = a + b
    # print(hasil)
    return hasil
    
result = sum(2, 3)
print(result)

# ======== MODULE FUNCTION =========== #
print('\n')
import mymodule as mm # module ini adalah file yang ada di mymodule.py

plus = mm.tambah(2, 5)
min = mm.kurang(2, 5)
multi = mm.kali(2, 5)
div = mm.bagi(2, 5)
ekponen = mm.pangkat(2, 5)

print(plus)
print(min)
print(multi)
print(div)
print(ekponen)