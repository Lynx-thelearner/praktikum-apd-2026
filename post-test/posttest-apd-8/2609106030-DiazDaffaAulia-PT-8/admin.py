import inquirer
import os

def menu_admin():
    os.system("cls" if os.name == "nt" else "clear")
    
    pertanyaan = [
        inquirer.List(
            'pilihan',
            message="Pilih Menu Admin",
            choices=[
                '1. Lihat Semua Pengguna',
                '2. Lihat Semua Tanaman',
                '3. Tambah Tanaman',
                '4. Edit Tanaman',
                '5. Hapus Tanaman',
                '6. Log Out'
            ]
        )
    ] 
            
    jawaban = inquirer.prompt(pertanyaan)
    return jawaban['pilihan'][0] if jawaban else '6'
