# ======= STRING MANIPULATION ========== #

name = 'Novrian Pratama'
print(name[0::2])

# (0::2) : penggunannya sama seperti range yaitu start,stop,step

#========= looping =========== #
str1 = "Machine Learning Engginer"
l = len(str1)
for i in range(l):
    print(str1[i])

# manipulation string
role = 'data science engginer, YES I AM'
print(role.upper()) # membuat tulisan menjadi kecil
print(role.lower()) # membuat tulisan menjadi Besar
print(role.title()) # membuat tulisan menjadi menjadi besar di awal tiap kata
print(role.capitalize()) # membuat tulisan menjadi besar diawal kalimat 

# String Function
print('\nString Advance Function')
learn = 'PythonPrograming'
mock = 'df'
print(learn.find('n', -2)) # cek value, jika tidak ada akan menghasilkan output -1
print(learn.index('P')) # cek lokasi index, jika tidak ada maka akan terjaid eror
print(learn.isalpha()) # cek apakah tulisan memiliki spasi atau tidak
print(mock.isdigit()) # cek apakah value memiliki angka atau tidak
print(mock.isalnum()) # cek apakah value memiliki angka atau tidak


# chr & ord function
print('\nchr & ord Function')
a = 3
print(chr(a)) # mengembalikan karakter (string) yang sesuai dengan nilai Unicode atau ASCII

b = 'n'
print(ord(b)) # mengembalikan nilai Unicode atau ASCII dari karakter tunggal yang diberikan.


# String Formatting
print('\nString Formatting')

role = ('Novrian Pratama sebagai {first} {Second}').format(first = 'Data', Second = 'Science')
role2 = ('Novrian Pratama sebagai {1} {0}').format('Data','Science') # mengambil data dengan index
role3 = ('Novrian Pratama sebagai {} {}').format('Data', 'Science') # otomatis terisi dengan index

print(role2)
print(role3)
