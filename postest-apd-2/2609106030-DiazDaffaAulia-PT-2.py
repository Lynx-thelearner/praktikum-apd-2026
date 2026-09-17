bagasi: list = [12, 18, 7, 15, 20, 10]
total_berat_akhir = bagasi[0] + bagasi[1] + bagasi[2] + bagasi[3] + bagasi[4] + bagasi[5]
total_bayar = total_berat_akhir * 5 / 100

rata_rata = total_berat_akhir / len(bagasi)

nim = 30
bolean_berat = nim < rata_rata

total_berat_akhir_gram = total_berat_akhir * 1000

print("List berat bagasi : ", bagasi,
     "\nSlicing bagasi : ", bagasi[2:5],
     "\ntotal berat akhir : ", total_berat_akhir,
     "\ntotal yang dibayar : ", total_bayar,
     "\nrata-rata berat bagasi : ", rata_rata,
     "\nnim : ", nim,
     "\nbolean berat : ", bolean_berat,
     "\ntotal berat akhir gram : ", total_berat_akhir_gram
)
