# batas = 5
# for i in range(batas):
#     print("perulangan ", i)

# nilai = [75, 60, 80, 60, 50]
# for item in nilai:
#     if item > 70:
#         print(item, "Lulus")
#     else:
#         print(item, "Tidak Lulus")
#
# for i in range(5, 0, -1): #Start, stop, step
#     print(i)

# for i in range(1, 3):# Mengontrol baris dalam tabel perkalian
#     for j in range(1, 4):# Mengontrol kolom dalam tabel perkalian
#         print(f'{i} x {j} = {i * j}')
#     print('') #biar ada jarak tiap iterasi

# jawab = "ya"
# hitung = 0

# while(jawab == "ya"):
#     hitung += 1
#     jawab = input("Ulang lagi tidak? ")

# print(f"Total Perulangan : {hitung}")
#
#
# for i in range(15):
#     if i == 10:
#         break
#     print(i)
#

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# for i in range(1, 4):
#     for j in range (1, 5):
#         print("*", end= ' ')

# n = int(input("Masukkan angka bulat"))
# ganjil = 0
# for i in range(1, n):
#     if n % 2 == 1:
#         ganjil += 1
#         print(i)
# print(f'jumlah ganjil: {ganjil}')
#

uang = int(input("Masukkan uang awalmu "))

while (uang >= 0):
    pengeluaran = int(input("Masukkan pengeluaran "))
    uang = uang - pengeluaran
    print("sisa uang", uang)
    if uang == 0:
        break
print("Saldo akhir", uang)
