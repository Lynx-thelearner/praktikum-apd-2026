from prettytable import PrettyTable
import inquirer

plants = {
    "1": {
        "nama": "Mandrake",
        "jenis": "Fantasy",
        "kondisi": "sehat"
    }
}

plant_id = 2

def tampil_semua_tanaman():
    print("=== Lihat Semua Tanaman ===")

    if not plants:
        print("Belum ada data tanaman")
        return
    table = PrettyTable(["ID", "Nama Tanaman", "Jenis", "Kondisi"])

    for pid, pdata in plants.items():
        table.add_row([pid, pdata["nama"], pdata["jenis"], pdata["kondisi"]])

    print(table)
    
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

        pertanyaan = [
            inquirer.List(
                'field',
                message="Pilih data yang mau diubah",
                choices=[
                    'Nama', 'Jenis', 'Kondisi'
                ]
            )
        ]

        jawaban = inquirer.prompt(pertanyaan)
        if not jawaban:
            return

        field = jawaban['field']
            
        if field == 'Nama':
            data_tanaman[pilih]["nama"] = input("Nama Baru: ")
            print("Nama berhasil diubah!")
        elif field == 'Jenis':
            data_tanaman[pilih]["jenis"] = input("Jenis Baru: ")
            print("Jenis berhasil diubah!")
        elif field == 'Kondisi':
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