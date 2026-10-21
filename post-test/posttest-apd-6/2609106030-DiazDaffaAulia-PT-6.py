import os

user = {
    "deez": {
        "password": "030",
        "role": "admin",
        "favorite": []
    },
    "naga": {
        "password": "123",
        "role": "member",
        "favorite": ["1"]
    }
}

plants = {
    "1": {
        "nama": "Mandrake",
        "jenis": "Fantasy",
        "kondisi": "sehat"
    }
}

username = ""
login = False
role_user = ""
plant_id = 2

while True:

    program = True

    while program:
        os.system("cls" if os.name == "nt" else "clear")

        print("===== Account Page =====")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Masukkan pilihan 1-3: ")

        if choice == "1":
            
            login = False
            role_user = ""
            
            for i in range(3):
                username = input("Masukkan Username: ").lower().strip()
                password = input("Masukkan Password: ")

                if username in user and user[username]["password"] == password:
                    login = True
                    role_user = user[username]["role"]
                        
                if login:
                    break

                elif i < 2:
                    print("Username atau Password salah")
                    input("Tekan untuk melanjutkan")
                else:
                    print("Kesempatan login habis")
                    input("Tekan untuk melanjutkan")

            if login:

                role = role_user
                
                if role == "admin":
                    print("Selamat datang, Endmin")
                    
                    
                else:
                    print("Selamat datang, member")

                input("Tekan untuk melanjutkan")
                break

        elif choice == "2":
            os.system("cls" if os.name == "nt" else "clear")

            username_baru = input("Masukkan username baru: ").lower().strip()
            password_baru = input("Masukkan password baru: ")

            if not username_baru or not password_baru:
                print("username atau password tidak boleh kosong")
            elif username_baru in user:
                print("username sudah digunakan")
            else:
                user[username_baru] = {
                    "password": password_baru,
                    "role": "member",
                    "favorite": []
                }
                print(f"Akun {username_baru} berhasil ditambahkan")

            input("Tekan untuk melanjutkan")

        elif choice == "3":
            os.system("cls" if os.name == "nt" else "clear")
            input("System Exit, byeee")
            program = False
            exit()

        else:
            print("Pilihan hanya 1-3")
            input("Tekan untuk melanjutkan")

    if login:
        role = role_user

        while True:
            os.system("cls" if os.name == "nt" else "clear")
    
            if role == "admin":
                print("="*5, " Menu Admin ", "="*5)
                print("1. Lihat semua pengguna")
                print("2. Lihat semua tanaman")
                print("3. Tambah Tanaman")
                print("4. Edit Tanaman")
                print("5. Hapus Tanaman")
                print("6. Log out")
    
                pilihan = input("Pilih menu : ")
    
                if pilihan == "1":
                    print("=== List Pengguna ===")

                    for uname, udata in user.items():
                        print("Username: ", uname)
                        print("Role: ", udata["role"])
                        print("Favorite: ", udata["favorite"])
                        print("-" * 10, "\n")

                    input("Tekan untuk melanjutkan")
                        
                elif pilihan == "2":
                    print("=== Lihat Semua Tanaman ===")

                    for pname, pdata in plants.items():
                        print("ID: ", pname)
                        print("Nama: ", pdata["nama"])
                        print("Jenis: ", pdata["jenis"])
                        print("Kondisi: ", pdata["kondisi"])
                        print("-" * 10, "\n")

                    input("Tekan untuk melanjutkan")

                elif pilihan == "3":
                    print("=== Tambah Tanaman ===")

                    new_nama = input("Masukkan Nama Tanaman : ")
                    new_jenis = input("Jenis tanaman apa? (ex. Bunga, Sayur, dll) : ")
                    new_kondisi = input("Masukkan Kondisi Tanaman : ")

                    if not new_nama or not new_jenis or not new_kondisi:
                        print("Semua input harus diisi")
                        input("Tekan untuk melanjutkan")

                    else:
                        plants[str(plant_id)] = {
                            "nama": new_nama,
                            "jenis": new_jenis,
                            "kondisi": new_kondisi
                        }

                        plant_id = plant_id + 1

                        print(f"Tanaman baru {new_nama} berhasil ditambahkan")

                    input("Tekan untuk melanjutkan")

                elif pilihan == "4":
                    print("=== Edit Tanaman ===")

                    for pname, pdata in plants.items():
                        print("ID: ", pname)
                        print("Nama: ", pdata["nama"])
                        print("Jenis: ", pdata["jenis"])
                        print("Kondisi: ", pdata["kondisi"])
                        print("-" * 10, "\n")

                    pilih = input("Masukkan ID Tanaman yang ingin diubah: ")
    
                    if pilih not in plants:
                        print("ID tidak ditemukan")
                        input("Tekan untuk melanjutkan")

                    else:
                        field = input("Pilih data yang mau diubah (1. Nama / 2. Jenis / 3. Kondisi): ").strip().lower()
                        
                        if field in ["1", "nama"]:
                                plants[pilih]["nama"] = input("Nama Baru: ")
                                print("Nama berhasil diubah!")
                        elif field in ["2", "jenis"]:
                                plants[pilih]["jenis"] = input("Jenis Baru: ")
                                print("Jenis berhasil diubah!")
                        elif field in ["3", "kondisi"]:
                                plants[pilih]["kondisi"] = input("Kondisi Baru: ")
                                print("Kondisi berhasil diubah!")
                        else:
                                print("Pilihan tidak valid.")
                        
                        input("\nTekan Enter untuk melanjutkan...")

                elif pilihan == "5":
                    print("=== Hapus Tanaman ===")

                    if len(plants) == 0:
                        print("Gada Tanaman yang bisa dihapus")
                    else:

                        for pname, pdata in plants.items():
                            print("ID: ", pname)
                            print("Nama: ", pdata["nama"])
                            print("Jenis: ", pdata["jenis"])
                            print("Kondisi: ", pdata["kondisi"])
                            print("-" * 10, "\n")
    
                        pilih = input("Masukkan ID Tanaman yang ingin dihapus: ")
        
                        if pilih not in plants:
                            print("ID Tidak Ditemukan")
        
                        else:
                            hapus = plants.pop(pilih)
                            print(f"Tanaman {hapus['nama']} berhasil dihapus")

                    input("\nTekan untuk melanjutkan...")

                elif pilihan == "6":
                    print("Logging Out...")
                    input("Tekan untuk melanjutkan...")
                    login = False
                    break

                else:
                    print("Pilihan tidak valid")
                    input("Tekan untuk melanjutkan")
                    
            else:
                print("="*5, " Menu ", "="*5)
                print("1. Lihat semua tanaman")
                print("2. Lihat Favorit")
                print("3. Tambah Favorit")
                print("4. Hapus Favorit")
                print("5. Log Out")

                pilihan = input("Pilih Menu : ")

                if pilihan == "1":
                    print("=== Lihat Semua Tanaman ===")

                    for pname, pdata in plants.items():
                        print("ID: ", pname)
                        print("Nama: ", pdata["nama"])
                        print("Jenis: ", pdata["jenis"])
                        print("Kondisi: ", pdata["kondisi"])
                        print("=" * 10, "\n")

                    input("Tekan untuk melanjutkan")

                elif pilihan == "2":
                    print("=== Favorit ===") 

                    favorit = user[username]["favorite"]

                    if len(favorit) == 0:
                        print("Gaada tanaman favorite.")
                    else:
                        for fid in favorit:
                            if fid in plants:
                                print("ID:", fid)
                                print("Nama:", plants[fid]["nama"])
                                print("Jenis:", plants[fid]["jenis"])
                                print("Kondisi:", plants[fid]["kondisi"])
                                print("=" * 5)

                    input("Tekan untuk melanjutkan")
                                
                elif pilihan == "3":
                    print("=== Tambah Favorit ===")

                    for pname, pdata in plants.items():
                        print("ID: ", pname)
                        print("Nama: ", pdata["nama"])
                        print("=" * 10, "\n")

                    pilih = input("Masukkan ID tanamannya: ")

                    if pilih not in plants:
                        print("ID tanaman gak ketemu")

                    elif pilih in user[username]["favorite"]:
                        print("Tanaman ini sudah ada di favorite")

                    else:
                        user[username]["favorite"].append(pilih)
                        print("Tanaman berhasil ditambahkan")

                    input("Tekan untuk melanjutkan")

                elif pilihan == "4":
                    print("=== Hapus Favorit ===")

                    favorit = user[username]["favorite"]
                    
                    if len(favorit) == 0:
                        print("Kamu belum punya tanaman favorit.")
                        
                    else:  
                        for pid in favorit:
                            if pid in plants:
                                print("ID:", pid)
                                print("Nama:", plants[pid]["nama"])
                                print("Jenis:", plants[pid]["jenis"])
                                print("Kondisi:", plants[pid]["kondisi"])
                                print("=" * 5)
                            else:
                                print("ID:", pid, "(Tanaman sudah dihapus dari katalog)")
                               
                        pilih = input("Masukkan ID tanaman yang ingin dihapus: ").strip()
    
                        if pilih not in favorit:
                            print("ID tidak ada di daftar favorit")
                        else:    
                            favorit.remove(pilih)
                            print("Tanaman berhasil dihapus dari favorit")

                    input("Tekan untuk melanjutkan")

                elif pilihan == "5":
                    print("logging out...")
                    input("Tekan untuk melanjutkan...")
                    login = False
                    break

                else:
                    print("Pilihan tidak valid")
                    input("Tekan untuk melanjutkan")