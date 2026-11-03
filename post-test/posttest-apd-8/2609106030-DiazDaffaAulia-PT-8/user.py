import inquirer
from prettytable import PrettyTable

from akun import user
import os

def menu_user():
        os.system("cls" if os.name == "nt" else "clear")

        pertanyaan = [
            inquirer.List(
                'pilihan',
                message="Pilih Menu User",
                choices=[
                    '1. Lihat Semua Tanaman',
                    '2. Lihat Favorit',
                    '3. Tambah Favorit',
                    '4. Hapus Favorit',
                    '5. Log Out'
                ]
            )
        ]

        jawaban = inquirer.prompt(pertanyaan)
        return jawaban['pilihan'][0] if jawaban else '5'


def tampil_semua_pengguna():
    print("=== List Pengguna ===")

    table = PrettyTable(["Username", "Role", "Favorite(ID)"])

    for uname, udata in user.items():
        fav_str = ", ".join(udata["favorite"]) if udata["favorite"] else "-"
        table.add_row([uname, udata["role"], fav_str])

    print(table)

    input("\nTekan untuk melanjutkan")
