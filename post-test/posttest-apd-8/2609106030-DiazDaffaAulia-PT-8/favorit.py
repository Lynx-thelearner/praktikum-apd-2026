from akun import user
from tanaman import plants
from prettytable import PrettyTable

def lihat_favorit(nama_user):
    print("=== Favorit ===")
    favorit = user[nama_user]["favorite"]
    
    if len(favorit) == 0:
            print("Gaada tanaman favorite.")
    else:

        table = PrettyTable(["ID", "Nama Tanaman", "Jenis", "Kondisi"])
        
        for fid in favorit:
            if fid in plants:
                table.add_row([fid, plants[fid]["nama"], plants[fid]["jenis"], plants[fid]["kondisi"]])
            else:
                table.add_row([fid, "(Tanaman dihapus dari katalog)", "-", "-"])
        print(table)
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