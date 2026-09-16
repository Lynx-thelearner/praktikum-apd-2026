bagasi: list = [12, 18, 7, 15, 20, 10]
total_berat_akhir = bagasi[0] + bagasi[1] + bagasi[2] + bagasi[3] + bagasi[4] + bagasi[5]
total_bayar = total_berat_akhir * 5 / 100

# 3. Hitung rata-rata berat bagasi per orang dengan membuat variabel bernama rata_rata
#  yang berisi variabel total_bayar dibagi dengan banyak data
# (diperbolehkan menggunakan fungsi len()). -Soal
#
# Saya ga paham, yang diminta variabel rata-rata berat bagasi per orang, tapi isi variabelnya pakai total_bayar,
# Itu bukannya jadi rata_rata total_bayar? Jadi aku buat 2 aja ya disini -Diaz
#
rata_rata_total_bayar = total_bayar / len(bagasi)
rata_rata_berat_bagasi = total_berat_akhir / len(bagasi)

nim = 30
bolean_bayar = nim < rata_rata_total_bayar
bolean_berat = nim < rata_rata_berat_bagasi

total_berat_akhir_gram = total_berat_akhir * 1000

print("List berat bagasi : ", bagasi,
     "\nSlicing bagasi : ", bagasi[2:5],
     "\ntotal berat akhir : ", total_berat_akhir,
     "\ntotal yang dibayar : ", total_bayar,
     "\nrata-rata bayar : ", rata_rata_total_bayar,
     "\nrata-rata berat bagasi : ", rata_rata_berat_bagasi,
     "\nnim : ", nim,
     "\nbolean bayar : ", bolean_bayar,
     "\nbolean berat : ", bolean_berat,
     "\ntotal berat akhir gram : ", total_berat_akhir_gram
)
