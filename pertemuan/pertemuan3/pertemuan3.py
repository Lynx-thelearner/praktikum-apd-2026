angka = 5

if angka < 10:
    print("Angka kurang dari 10")


if 1 == "1":
    print(True)
else:
    print(False)

umur = int(input("Masukkan umur:"))

if umur >= 17:
    print("Udah bisa buat KTP")
else:
    print("Belum bisa buat ktp")


print("mobil, motor, lainnya.")
kendaraan = input("Masukkan kendaraan: ")
kendaraan = kendaraan.lower()

if kendaraan == "mobil":
    tarif_parkir = 10000
elif kendaraan == "motor":
    tarif_parkir = 5000
else:
    tarif_parkir = 15000

print("Tarif parkir: ", tarif_parkir)

nilai = int(input("Masukkan nilai: "))
status = "lulus" if nilai >= 80 else "tidak lulus"
print("Status: ", status)

nilai_siswa = int(input("Masukkan nilai siswa: "))

if nilai_siswa >= 10:
    if nilai_siswa >= 20:
        if nilai_siswa >= 30:
            print("Angka besar")
        print("Angka sedang")
    print("Angka kecil")

usia = int(input("Masukkan usia: "))
status_usia = "Boleh masuk" if usia >= 16 else "Tidak boleh masuk"
print("Status usia: ", status_usia)


total_harga = int(input("Masukkan total harga: "))
if total_harga >= 200000:
    print("Diskon 30%")
elif total_harga >= 100000:
    print("Diskon 10%")
else:
    print("Tidak ada diskon")
