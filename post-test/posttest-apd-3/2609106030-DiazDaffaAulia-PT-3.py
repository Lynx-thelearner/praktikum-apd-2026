nickname = "deez"
nim = "30"

print("===============SELAMAT DATANG DI PERTAMINI=======================")
nama = input("Masukkan nama mu : ").lower()
nimi = input("Masukkan 2 digit terakhir NIM : ")

login = nama == nickname and nimi == nim
if not login:
    print("Login gagal")
    exit()

print(f"\nLogin berhasil \nMet datang kembali {nama}")

print("\n=================PILIH JENIS BBM=======================")
print("Pertalite 10.000/liter(1)" \
      "\nPertamax 12.500/liter(2)" \
      "\nPertamax Turbo 15.000/liter(3)")

pilihan = input("Masukkan pilihan(1/2/3) : ")
liter = float(input("Masukkan jumlah liter : "))

if pilihan == "1":
    bbm = "Pertalite"
    harga = 10000
elif pilihan == "2":
    bbm = "Pertamax"
    harga = 12500
elif pilihan == "3":
    bbm = "Pertamax Turbo"
    harga = 15000
else:
    print("\nPilihannya 1 - 3")
    exit()

total_harga = harga * liter

if liter >= 10:
    diskon = 0.10
elif liter >= 5:
    diskon = 0.05
else:
    diskon = 0

diskon_liter = diskon * total_harga

print("\n======STATUS ANGGOTA======")

member = input("Apakah anda member? (y/t) : ").lower()

if member == "y": 
    diskon_member = 0.02 * total_harga
    status = "Member"
elif member == "t":
    diskon_member = 0
    status = "Non-Member"
else:
    print("Input tidak valid")
    exit()

total_diskon = diskon_liter + diskon_member
total_bayar = total_harga - total_diskon

print("\n======== HASIL TRANSAKSI ========")
print(f"{'Nama':<18}: {nama}")
print(f"{'NIM':<18}: {nimi}")
print(f"{'Jenis BBM':<18}: {bbm}")
print(f"{'Liter':<18}: {liter}")    
print(f"{'Status':<18}: {status}")
print("---------------------------------")
print(f"{'Total Harga':<18}: Rp{total_harga:,.0f}")
print(f"{'Diskon BBM':<18}: Rp{diskon_liter:,.0f}")
print(f"{'Diskon Member':<18}: Rp{diskon_member:,.0f}")
print(f"{'Total Diskon':<18}: Rp{total_diskon:,.0f}")
print(f"{'Total Bayar':<18}: Rp{total_bayar:,.0f}")
print("=================================")
