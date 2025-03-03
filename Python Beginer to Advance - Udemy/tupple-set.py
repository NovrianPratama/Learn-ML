tup = (32, 3, 4, 5, 6, 76, 43, 2, 12)
print(tup, type(tup))
length = len(tup)

for i in range(length):
    print(i, tup[i])

maxx = max(tup)
minn = min(tup)
print(minn)
print(tup.index(5)) # mencari urutan index dengan parameter value


# =========== SET ============= #
print('\nSet')
data_set = {3, 4, 5, 12, 34, 5, 3, 23, 1}

print(data_set, type(data_set))

for i in data_set:
    print(i) # jika menggunakan print(data_set[i]) = akan error karena set tidak menggunakan index

data_set.pop()
# data_set.clear()
data_set.add(66)

list1 = [3, 4, 5, 5, 66, 445, 31]
data_set.update(list1) # menambahkan data baru
print(data_set)