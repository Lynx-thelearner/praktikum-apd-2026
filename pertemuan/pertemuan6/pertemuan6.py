kartu = ["merah", "merah", "biru", "hijau"]
# print(kartu)

set_kartu = set(kartu)
# print(set_kartu)

set_kartu.add("kuning")

# print(len(set_kartu))
# print(len(kartu))

for i in set_kartu:
    print(i)


# aslab1 = {"fina", "shasha", "risma"}
# aslab2 = {"larry", "attar", "haekal"}
# gabung = aslab1.union(aslab2)
# print(gabung)

# Biodata = {
# "Nama" : "Siti Julpa",
# "NIM" : 25091060,
# "KRS" : ["Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" : True,
# "Instagram" : "julpatarr"
# }

# print(Biodata["KRS"])


game = {
    "pou": "chill",
    "genshin impact": "action",
    "valorant": "fps",
    "minecraft": "sandbox",
    "mobile legend": "moba",
}

# for i in game.values():
#     print(i)

# for i in game.keys():
#     print(i)

# for i, j in game.items():
#     print(f"{i} adalah jenis game {j}")

# game["resident evil"] = "horror"
# print(game)

# game.update({
#     "ML" : "MOBA",
#     "Stardew Valley" : "Farm and chill"
# })

# print(game)


# data_siswa = {
#     "siswa1" : {
#         "nama" : "Johan",
#         "Kelas" : "A2",
#         "Nilai" : 95
#     },

#     "siswa2" : {
#         "nama" : "Niyah",
#         "Kelas" : "A2",
#         "Nilai" : 96
#     }
# }

# print(data_siswa["siswa1"])
