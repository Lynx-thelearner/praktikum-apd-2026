from tanaman import edit_tanaman, hapus_tanaman, tambah_tanaman, tampil_semua_tanaman, plants
from akun import menu_akun, login_user, register_user, username, role, user
from admin import menu_admin
from user import tampil_semua_pengguna, menu_user
from favorit import hapus_favorit, lihat_favorit, tambah_favorit
import os

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
                pilihan = menu_user()

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
