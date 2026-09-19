bagasi_1 = 12
bagasi_2 = 18
bagasi_3 = 7
bagasi_4 = 15
bagasi_5 = 20
bagasi_6 = 10

bagasi = [bagasi_1, bagasi_2, bagasi_3, bagasi_4, bagasi_5, bagasi_6]

total_berat_akhir = bagasi[0] + bagasi[1] + bagasi[2] + bagasi[3] + bagasi[4] + bagasi[5]

total_bayar = total_berat_akhir * 5 / 100

rata_rata = total_berat_akhir / len(bagasi)

nim = 30
bolean = nim < rata_rata

total_berat_akhir_gram = total_berat_akhir * 1000

print("Bagasi 1 : ", bagasi_1,
    "\nBagasi 2 : ", bagasi_2,
    "\nBagasi 3 : ", bagasi_3,
    "\nBagasi 4 : ", bagasi_4,
    "\nBagasi 5 : ", bagasi_5,
    "\nBagasi 6 : ", bagasi_6,
    "\nList berat bagasi : ", bagasi,
    "\nSlicing bagasi : ", bagasi[2:5],
    "\nTotal berat akhir : ", total_berat_akhir,
    "\nTotal yang dibayar : ", total_bayar,
    "\nRata-rata berat bagasi : ", rata_rata,
    "\nNIM : ", nim,
    "\nBolean : ", bolean,
    "\nTotal berat akhir gram : ", total_berat_akhir_gram
)
