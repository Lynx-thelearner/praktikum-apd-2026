import os
import inquirer
from pwinput import pwinput

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

username = ""
role = ""

def menu_akun():
    os.system("cls" if os.name == "nt" else "clear")

    pertanyaan = [
        inquirer.List(
            'pilihan',
            message="Pilih Menu Akun",
            choices=[
                '1. Login',
                '2. Register',
                '3. Exit'
            ]
        )
    ]

    jawaban = inquirer.prompt(pertanyaan)
    return jawaban['pilihan'][0] if jawaban else '3'

def login_user(max_percobaan):
    for i in range(max_percobaan):
        try:
            username = input("Masukkan Username: ").lower().strip()  
            password = pwinput(prompt="Masukkan Password: ", mask="*")

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
    password_baru = pwinput(prompt="Masukkan password baru: ", mask="*")

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