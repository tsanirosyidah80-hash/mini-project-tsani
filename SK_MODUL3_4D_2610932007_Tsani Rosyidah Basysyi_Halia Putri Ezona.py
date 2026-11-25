import csv
import os

# 1. Membaca file CSV
data = []

with open("data_kualitas.csv", "r") as file:
    pembaca = csv.DictReader(file)

    for baris in pembaca:
        data.append(baris)

# 2. Memeriksa apakah data tersedia
if len(data) == 0:
    print("Data CSV kosong")

else:
    total_produksi = 0
    total_cacat = 0

    # Array untuk menyimpan jenis cacat
    jenis = ["gores", "retak", "warna", "dimensi"]
    jumlah_jenis = [0, 0, 0, 0]

    produksi_A = 0
    cacat_A = 0
    produksi_B = 0
    cacat_B = 0

    print("=== ANALISIS KUALITAS PRODUK ===")

    # 3. Mengolah setiap baris data
    for baris in data:
        try:
            produksi = int(baris["jumlah_produksi"])
            cacat = int(baris["jumlah_cacat"])
            shift = baris["shift"].strip().upper()
            nama_jenis = baris["jenis_cacat"].strip().lower()
            tanggal = baris["tanggal"].strip()
            lot = baris["lot"].strip()

            # Validasi data sederhana
            if (produksi <= 0 or cacat < 0 or cacat > produksi
                    or shift not in ["A", "B"] or not lot
                    or not tanggal or nama_jenis not in jenis):
                print("Data tidak valid:", lot)
                continue

            total_produksi += produksi
            total_cacat += cacat

            # Menghitung jumlah setiap jenis cacat
            for i in range(len(jenis)):
                if nama_jenis == jenis[i]:
                    jumlah_jenis[i] += cacat

            # Menghitung berdasarkan shift
            if shift == "A":
                produksi_A += produksi
                cacat_A += cacat
            else:
                produksi_B += produksi
                cacat_B += cacat

            # Menghitung tingkat cacat per lot
            tingkat = cacat / produksi * 100

            print("\nLot:", lot)
            print("Tanggal:", tanggal)
            print("Shift:", shift)
            print("Jumlah produksi:", produksi)
            print("Jumlah cacat:", cacat)
            print("Jenis cacat:", nama_jenis)
            print("Tingkat cacat:", round(tingkat, 2), "%")

        except (ValueError, KeyError):
            print("Data tidak valid atau format salah")

    # 4. Menampilkan hasil analisis
    print("\n=== HASIL KESELURUHAN ===")

    if total_produksi > 0:
        tingkat_total = total_cacat / total_produksi * 100

        print("Total produksi:", total_produksi)
        print("Total cacat:", total_cacat)
        print("Tingkat cacat:", round(tingkat_total, 2), "%")

        print("\n=== JUMLAH CACAT PER JENIS ===")

        for i in range(len(jenis)):
            print(jenis[i].title(), ":", jumlah_jenis[i], "unit")

        # Menentukan jenis cacat terbanyak
        terbesar = 0

        for i in range(1, len(jenis)):
            if jumlah_jenis[i] > jumlah_jenis[terbesar]:
                terbesar = i

        print("\nJenis cacat terbanyak:",
              jenis[terbesar].title(),
              "-", jumlah_jenis[terbesar], "unit")

        print("\n=== ANALISIS PER SHIFT ===")

        if produksi_A > 0:
            persen_A = cacat_A / produksi_A * 100
            print("Shift A:", round(persen_A, 2), "% tingkat cacat")

        if produksi_B > 0:
            persen_B = cacat_B / produksi_B * 100
            print("Shift B:", round(persen_B, 2), "% tingkat cacat")

    else:
        print("Tidak ada data valid untuk dianalisis")