tup = (1, 2, 3, 4)
result = min(tup)
print(result)
# ----------------------------------------------------------
tup = (80, 90, 85, 60, 75)
mean = sum(tup)/len(tup)
print(mean)
# ----------------------------------------------------------
tup = ("andi", "galang", "ucup", "udin", "salsa")
k = input("Cari nama: ")
j = k in tup
if j:
    print(f'Nama {k} ditemukan')
else:
    print(f'Nama {k} tidak ditemukan')
