# ==================== if,else,elif ===============#

print('Kalkulator')

val1 = eval(input('Masukkan Angka pertama: '))
val2 = eval(input('Masukkan Angka kedua: '))
oper = input('Masukkan Operatornya: ')

if oper == '+':
    result = val1 + val2
    print(f"Hasil: {result}")
elif oper == '-':
    result = val1 - val2
    print(f"Hasil: {result}")
elif oper == '*':
    result = val1 * val2
    print(f"Hasil: {result}")
elif oper == '/':
    result = val1 / val2
    print(f"Hasil: {result}")
else:
    print("Masukkan ulang operatornya!")
    
    
