#Post test bagian perulanga (God help me)
nama = "deez"
password = "030"

print("======Login Page=====")
for i in range(3):
    username = input("Masukkan Nama : ").lower()
    nimi = input("Masukkan nimi : ")
    
    if nama == username and password == nimi:
        print("Login Berhasil, met datang kembali ", username)
        break
    else: 
        if i < 2:
            print("Nama atau password salah, silahkan coba lagi")
        else:
            print("Kesempatan login habis, sistem berakhir.")
            exit()
                        
data_siswa = []
data_kelas = []

print("=====Masukkan Data Siswa=====")
while True:

    nama_siswa = input("Masukkan Nama Siswa : ")
    kelas_siswa = input("Masukkan Kelas Siswa : ").upper()

    while True:
        ujian = input(f"apakah {nama_siswa} mengikuti ujian? (ya/tidak) ").lower()

        if ujian == "ya":
            print("Dia ikut ujian")

            while True:
                soal_benar = int(input("Masukkan soal benar (0-20) "))

                if 0 <= soal_benar <= 20:
                    break
                else:
                    print("Jumlah soal benar harus antara 0 dan 20")
            
            soal_salah = 20 - soal_benar
            nilai_akhir = soal_benar * 5

            if nilai_akhir >= 80:
                kategori = "Sangat Baik"
            elif nilai_akhir >= 60:
                kategori = "Baik"
            elif nilai_akhir >= 40:
                kategori = "Cukup"
            else:
                kategori = "Perlu belajar lagi"
                
            break
                
        elif ujian == "tidak":
            nilai_akhir = 0
            kategori = "Tidak mengikuti ujian"
            break
        else:
            print("Pilihannya hanya 'ya' dan 'tidak'")

    data_siswa.append([
        nama_siswa,
        kelas_siswa,
        ujian,
        nilai_akhir,
        kategori
    ])
    
    if kelas_siswa not in data_kelas:
        data_kelas.append(kelas_siswa)

    
    while True:    
        lanjut_lagi = input("Ulang lagi? (y/t) ").lower()

        if lanjut_lagi == "y" or lanjut_lagi == "t":
            break
        else:
            print("Silahkan coba lagi")

    if lanjut_lagi == "t":
        break
        

print("\n=====Data Nilai Siswa=====")

for kelas in data_kelas:
    print(f"\n=====Kelas {kelas}=====")
    for siswa in data_siswa:
        if siswa[1] == kelas:
            print(f"Nama : {siswa[0]}"
                  f"\nKelas : {siswa[1]}"
                  f"\nIkut Ujian : {siswa[2]}"
                  f"\nNilai : {siswa[3]} ({siswa[4]})"
                  "\n-------------------")

#Alhamdulillah selesai