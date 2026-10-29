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

plant_id = 2
username = ""
role = ""

def menu_akun():
    os.system("cls" if os.name == "nt" else "clear")
    print("===== Account Page =====")
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    choice = input("Masukkan pilihan 1-3: ")
    return choice

def menu_admin():
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 5, " Menu Admin ", "=" * 5)
    print("1. Lihat semua pengguna")
    print("2. Lihat semua tanaman")
    print("3. Tambah Tanaman")
    print("4. Edit Tanaman")
    print("5. Hapus Tanaman")
    print("6. Log out")
    pilihan = input("Pilih menu : ") 
    return pilihan

def tampil_semua_pengguna():
    print("=== List Pengguna ===")
    for uname, udata in user.items():
        print("Username: ", uname)
        print("Role: ", udata["role"])
        print("Favorite: ", udata["favorite"])
        print("-" * 10, "\n")
    input("Tekan untuk melanjutkan")

def tampil_semua_tanaman():
    print("=== Lihat Semua Tanaman ===")
    for pname, pdata in plants.items():
        print("ID: ", pname)
        print("Nama: ", pdata["nama"])
        print("Jenis: ", pdata["jenis"])
        print("Kondisi: ", pdata["kondisi"])
        print("-" * 10, "\n")

def login_user(max_percobaan):
    for i in range(max_percobaan):
        try:
            username = input("Masukkan Username: ").lower().strip()  
            password = input("Masukkan Password: ")  

            if username in user and user[username]["password"] == password:
                role = user[username]["role"]  
                if role == "admin":
                    print("Selamat datang, Endmin")
                else:
                    print("Selamat datang, member")
                input("Tekan untuk melanjutkan")
                return username, role

        except KeyError:
            print("Terjadi kesalahan pada data pengguna")
            input("Tekan untuk melanjutkan")
            continue

        if i < max_percobaan - 1:
            print("Username atau Password salah")
            input("Tekan untuk melanjutkan")
        else:
            print("Kesempatan login habis")
            input("Tekan untuk melanjutkan")

    return None, None

def register_user(data_user):
    os.system("cls" if os.name == "nt" else "clear")

    username_baru = input("Masukkan username baru: ").lower().strip()
    password_baru = input("Masukkan password baaru: ")

    try:
        if not username_baru or not password_baru:
            raise ValueError("Username atau password tidak boleh kosong")

        if username_baru in data_user:
            print("Username sudah digunakan")
        else:
            data_user[username_baru] = {
                "password": password_baru,
                "role": "member",
                "favorite": []
            }
            print(f"Akun {username_baru} berhasil ditambahkan")

    except ValueError as e:
        print(e)

    input("Tekan untuk melanjutkan")

def tambah_tanaman(data_tanaman):
    global plant_id
    print("=== Tambah Tanaman ===")

    new_nama = input("Masukkan Nama Tanaman : ")
    new_jenis = input("Jenis tanaman apa? (ex. Bunga, Sayur, dll) : ")
    new_kondisi = input("Masukkan Kondisi Tanaman : ")

    try:
        if not new_nama or not new_jenis or not new_kondisi:
            raise ValueError("Semua input harus diisi")

        data_tanaman[str(plant_id)] = {
            "nama": new_nama,
            "jenis": new_jenis,
            "kondisi": new_kondisi
        }
        plant_id += 1
        print(f"Tanaman baru {new_nama} berhasil ditambahkan")

    except ValueError as e:
        print(e)

    input("Tekan untuk melanjutkan")

def edit_tanaman(data_tanaman):
    print("=== Edit Tanaman ===")
    tampil_semua_tanaman()

    pilih = input("Masukkan ID tanaman yang ingin diubah: ")

    if pilih not in data_tanaman:
        print("ID tidak ditemukan")
        input("Tekan untuk melanjutkan")
    else:
        field = input("Pilih data yang mau diubah (1. Nama / 2. Jenis / 3. Kondisi): ").strip().lower()

        if field in ["1", "nama"]:
            data_tanaman[pilih]["nama"] = input("Nama Baru: ")
            print("Nama berhasil diubah!")
        elif field in ["2", "jenis"]:
            data_tanaman[pilih]["jenis"] = input("Jenis Baru: ")
            print("Jenis berhasil diubah!")
        elif field in ["3", "kondisi"]:
            data_tanaman[pilih]["kondisi"] = input("Kondisi Baru: ")
            print("Kondisi berhasil diubah!")
        else:
            print("Pilihan tidak valid.")

        input("\nTekan Enter untuk melanjutkan...")

def hapus_tanaman(data_tanaman):
    print("=== Hapus Tanaman ===")

    if len(data_tanaman) == 0:
        print("Gada Tanaman yang bisa dihapus")
    else:
        tampil_semua_tanaman()
        pilih = input("Masukkan ID Tanaman yang ingin dihapus: ")

        if pilih not in data_tanaman:
            print("ID Tidak Ditemukan")
        else:
            hapus = data_tanaman.pop(pilih)
            print(f"Tanaman {hapus['nama']} berhasil dihapus")

    input("\nTekan untuk melanjutkan...")

def lihat_favorit(nama_user):
    print("=== Favorit ===")
    favorit = user[nama_user]["favorite"]
    
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

def tambah_favorit(nama_user):
    print("=== Tambah Favorit ===")

    for pname, pdata in plants.items():
        print("ID: ", pname)
        print("Nama: ", pdata["nama"])
        print("=" * 10, "\n")

    pilih = input("Masukkan ID tanamannya: ")

    if pilih not in plants:
        print("ID tanaman gak ketemu")
    elif pilih in user[nama_user]["favorite"]:
        print("Tanaman ini sudah ada di favorite")
    else:
        user[nama_user]["favorite"].append(pilih)
        print("Tanaman berhasil ditambahkan")

    input("Tekan untuk melanjutkan")

def hapus_favorit(nama_user):
    print("=== Hapus Favorit ===")
    favorit = user[nama_user]["favorite"]

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


while True:

    program = True

    while program:
        choice = menu_akun()

        if choice == "1":
            username, role = login_user(3)

            if username is not None:
                break

        elif choice == "2":
            register_user(user)

        elif choice == "3":
            os.system("cls" if os.name == "nt" else "clear")
            input("System Exit, byeee")
            exit()

        else:
            print("Pilihan hanya 1-3")
            input("Tekan untuk melanjutkan")

    if username is not None and role is not None:

        while True:
            if role == "admin":
                pilihan = menu_admin()

                if pilihan == "1":
                    tampil_semua_pengguna()

                elif pilihan == "2":
                    tampil_semua_tanaman()
                    input("Tekan untuk melanjutkan")

                elif pilihan == "3":
                    tambah_tanaman(plants)

                elif pilihan == "4":
                    edit_tanaman(plants)

                elif pilihan == "5":
                    hapus_tanaman(plants)

                elif pilihan == "6":
                    print("Logging Out...")
                    input("Tekan untuk melanjutkan...")
                    break

                else:
                    print("Pilihan tidak valid")
                    input("Tekan untuk melanjutkan")

            else:
                os.system("cls" if os.name == "nt" else "clear")
                print("=" * 5, " Menu ", "=" * 5)
                print("1. Lihat semua tanaman")
                print("2. Lihat Favorit")
                print("3. Tambah Favorit")
                print("4. Hapus Favorit")
                print("5. Log Out")

                pilihan = input("Pilih Menu : ")

                if pilihan == "1":
                    tampil_semua_tanaman()
                    input("Tekan untuk melanjutkan")

                elif pilihan == "2":
                    lihat_favorit(username)

                elif pilihan == "3":
                    tambah_favorit(username)

                elif pilihan == "4":
                    hapus_favorit(username)

                elif pilihan == "5":
                    print("logging out...")
                    input("Tekan untuk melanjutkan...")
                    break

                else:
                    print("Pilihan tidak valid")
                    input("Tekan untuk melanjutkan")
