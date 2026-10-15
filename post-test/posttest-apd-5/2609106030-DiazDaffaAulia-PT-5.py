
import os

user = [
    ["deez", "030", "admin"],
    ["naga", "123", "member"]
]

plants = [
    ["Mandrake", "Fantasy", "sehat"]
]

login = False
role_akun = ""

while True:

    program = True
    
    while program:
        os.system("cls" if os.name == "nt" else "clear")
    
        print("====== Account Page ======")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
    
        account_choice = input("Masukkan pilihan 1-3: ")
    
        if account_choice == "1":
            login = False
            role_akun = ""
    
            for i in range(3):
                username = input("Masukkan Username: ").lower()
                password = input("Masukkan Password: ")
    
                for akun in user:
                    if akun[0] == username and akun[1] == password:
                        login = True
                        role_akun = akun
                        break
    
                if login:
                    break
                elif i < 2:
                    print("Username atau password salah, coba lagi.")
                else:
                    print("Kesempatan login habis.")
                    input("Tekan Enter untuk kembali ke menu...")
    
            if login:
                role = role_akun[2]
    
                if role == "admin":
                    print("Selamat datang, Admin!")
                else:
                    print("Selamat datang, Member!")
    
                input("Tekan Enter untuk melanjutkan")
                break
    
        elif account_choice == "2":
            username = input("Masukkan Username: ").lower().strip()
    
            if username == "":
                print("Username tidak boleh kosong.")
                input("Enter to continue")
            else:
                username_ada = False
        
                for akun in user:
                    if akun[0] == username:
                        username_ada = True
                        break
        
                if username_ada:
                    print("Username sudah digunakan.")
                else:
                    password = input("Masukkan Password: ")
                    new_user = [username, password, "member"]
                    user.append(new_user)
                    print("Registrasi berhasil! Silakan login.")
        
                input("Tekan Enter untuk kembali ke menu...")
    
        elif account_choice == "3":
            print("System Exit, byeee")
            program = False
            exit()
    
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk kembali...")
    
    
    if login:
        role = role_akun[2]
    
        while True:
            os.system("cls" if os.name == "nt" else "clear")
    
            if role == "admin":
                print("="*5, " Menu Admin ", "="*5)
                print("1. Lihat semua pengguna")
                print("2. Lihat semua tanaman")
                print("3. Logout")
    
                pilihan = input("Pilih menu : ")
    
                if pilihan == "1":
                    print("=== List User ===")
                
                    for akun in user:
                        print("Username:", akun[0])
                        print("Role:", akun[2])
                        print("-" * 20)
                    
                    input("Tekan Enter untuk kembali...")
    
                elif pilihan == "2":
                    print("=== List Tanaman ===")
                
                    if len(plants) == 0:
                        print("Koleksi tanaman masih kosong.")
                    else:
                        for tanaman in plants:
                            print(tanaman)
                            
                    input("\nTekan Enter untuk kembali...")
    
                elif pilihan == "3":
                    print("Logout berhasil!")
                    input("Tekan Enter untuk melanjutkan...")
                    login = False
                    break
    
                else:
                    print("Pilihan menu tidak valid!")
                    input("Tekan Enter untuk kembali...")
                
            else:
                print("="*10, " Menu Member ", "="*10)
                print("1. Lihat koleksi tanaman")
                print("2. Tambah tanaman")
                print("3. Perbarui kondisi tanaman")
                print("4. Hapus tanaman")
                print("5. Logout")
    
                pilihan = input("Pilih menu : ")
    
                if pilihan == "1":
                    print("=== List Tanaman ===")
                    if len(plants) == 0:
                        print("Koleksi tanaman masih kosong.")
                    else:
                        for tanaman in plants:
                            print(tanaman)
                    input("Kembali.")
    
                elif pilihan == "2":
                    print("=== Tambah Tanaman ===")
    
                    nama = input("Nama tanaman: ")
                    jenis = input("Jenis tanaman: ")
                    kondisi = input("Kondisi tanaman: ")
                    
                    new_tanaman = [nama, jenis, kondisi]
                    plants.append(new_tanaman)
                    
                    print(plants)
    
                    input("Enter to continue")
                
                elif pilihan == "3":
                    print("=== Perbarui Tanaman ===")
    
                    if len(plants) == 0:
                            print("Belum ada tanaman untuk diperbarui.")
                    
                    else:
                        for i in range(len(plants)):
                            print(i + 1, ".", plants[i])
                    
                        nomor = input("Pilih nomor tanaman: ")
                    
                        if nomor.isdigit():
                            nomor = int(nomor)
                    
                            if nomor >= 1 and nomor <= len(plants):
                                indeks = nomor - 1
                    
                                print("Data saat ini:", plants[indeks])
                    
                                nama = input("Nama baru: ")
                                jenis = input("Jenis baru: ")
                                kondisi = input("Kondisi baru: ")
                    
                                plants[indeks][0] = nama
                                plants[indeks][1] = jenis
                                plants[indeks][2] = kondisi
                    
                                print("Tanaman berhasil diperbarui!")
                           
                            else:
                                print("Nomor tanaman gada.")
        
                        else:
                            print("Masukkannya harus angka.")
                
                    input("Tekan Enter untuk kembali...")
    
                elif pilihan == "4":
                    print("=== Hapus Tanaman ===")
    
                    if len(plants) == 0:
                        print("Kamu gaada tanaman, apa yang mau dihapus")
                    else:
    
                        for i in range(len(plants)):
                            print(i + 1, ".", plants[i])
        
                        nomor = input("Tanaman nomor berapa? ")
        
                        if nomor.isdigit():
                            nomor = int(nomor)
        
                            if nomor >= 1 and nomor <= len(plants):
                                indeks = nomor - 1
        
                                tanaman_dihapus = plants.pop(indeks)
                                
                                print("Tanaman", tanaman_dihapus[0], "telah dihapus.")
                            else:
                                print("Tanaman enggak ditemukan")
                        else:
                            print("masukin angka.")
    
                    input("Enter to continue")
    
                elif pilihan == "5":
                    print("Logout berhasil!")
                    input("Tekan Enter untuk melanjutkan...")
                    login = False
                    break
    
                else:
                    print("Pilihan menu tidak valid!")
                    input("Tekan Enter untuk kembali...")
    
                        