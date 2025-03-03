import random

# random randint = menghasilkan angkar random dari range 1-10 secara acark
print('Random int', random.randint(1, 10))
# randrange = menghasilkan bilangan random dengan parameter (start, stop, step)
print('Random Range', random.randrange(5, 20, 3))

list1 = [12, 3, 4, 2, 6, 7, 35, 23, 25, 16]
# choice = memilih angka secara acara pada value list
print('Random choice', random.choice(list1)) 

# random = menghasilkan angka random dengan rentang 0-1
print('Random Random', random.random()) # tidak ada parameter

# Shuffle = untuk mengacak angka pada value list
random.shuffle(list1)
print('Random Shuffle', list1) 

# Uniform = menghasilkan bilangan acak dalam bentuk float dalam rentang tertentu
print('Uniform', random.uniform(1, 10))