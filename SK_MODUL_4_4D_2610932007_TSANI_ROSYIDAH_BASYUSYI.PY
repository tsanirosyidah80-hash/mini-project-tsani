import csv

FILE_CSV = "data_kualitas.csv"

# 1. Membaca file CSV
data = []

try:
    with open(FILE_CSV, "r", encoding="utf-8-sig") as file:
        pembaca = csv.DictReader(file)

        for baris in pembaca:
            data.append(baris)

except FileNotFoundError:
    print("File CSV tidak ditemukan")

else:

    # 2. Memeriksa apakah data tersedia
    if len(data) == 0:
        print("Data CSV kosong")

    else:
        total_produksi = 0
        total_cacat = 0

        # Array jenis cacat
        jenis = ["gores", "retak", "warna", "dimensi"]
        jumlah_jenis = [0, 0, 0, 0]

        produksi_A = 0
        cacat_A = 0
        produksi_B = 0
        cacat_B = 0

        # Array untuk menyimpan hasil setiap lot
        hasil_lot = []

        # 3. Mengolah setiap baris data
        for baris in data:
            try:
                produksi = int(baris["jumlah_produksi"])
                cacat = int(baris["jumlah_cacat"])
                shift = baris["shift"].strip().upper()
                nama_jenis = baris["jenis_cacat"].strip().lower()
                tanggal = baris["tanggal"].strip()
                lot = baris["lot"].strip()

                # Validasi data
                if (produksi <= 0 or cacat < 0
                    or cacat > produksi
                    or shift not in ["A", "B"]
                    or not lot or not tanggal
                    or nama_jenis not in jenis):

                    print("Data tidak valid:", lot)
                    continue

                total_produksi += produksi
                total_cacat += cacat

                # Menghitung cacat berdasarkan jenis
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

                # Menghitung tingkat cacat
                tingkat = cacat / produksi * 100

                # Menyimpan hasil ke array
                hasil_lot.append([
                    lot, tanggal, shift, produksi,
                    cacat, nama_jenis, round(tingkat, 2)
                ])

            except (ValueError, KeyError, AttributeError):
                print("Data tidak valid atau format salah")

        # 4. Menampilkan tabel hasil setiap lot
        print("\n========== ANALISIS KUALITAS PRODUK ==========")

        if len(hasil_lot) > 0:

            print("\nTABEL DATA KUALITAS PRODUK")
            print("-" * 100)

            print(
                f"{'Lot':<10}"
                f"{'Tanggal':<15}"
                f"{'Shift':<8}"
                f"{'Produksi':<12}"
                f"{'Cacat':<10}"
                f"{'Jenis Cacat':<15}"
                f"{'Tingkat (%)':<12}"
            )

            print("-" * 100)

            for baris in hasil_lot:
                print(
                    f"{baris[0]:<10}"
                    f"{baris[1]:<15}"
                    f"{baris[2]:<8}"
                    f"{baris[3]:<12}"
                    f"{baris[4]:<10}"
                    f"{baris[5]:<15}"
                    f"{baris[6]:<12}"
                )

            print("-" * 100)

        # 5. Menampilkan hasil keseluruhan
        print("\nTABEL HASIL KESELURUHAN")

        if total_produksi > 0:

            tingkat_total = total_cacat / total_produksi * 100

            print("-" * 55)
            print(f"{'Keterangan':<30}{'Jumlah':>15}")
            print("-" * 55)

            print(f"{'Total Produksi':<30}{total_produksi:>15}")
            print(f"{'Total Produk Cacat':<30}{total_cacat:>15}")
            print(f"{'Tingkat Cacat (%)':<30}{round(tingkat_total, 2):>15}")

            print("-" * 55)

            # 6. Tabel jumlah cacat per jenis
            print("\nTABEL JUMLAH CACAT PER JENIS")
            print("-" * 40)
            print(f"{'Jenis Cacat':<20}{'Jumlah Cacat':>15}")
            print("-" * 40)

            for i in range(len(jenis)):
                print(
                    f"{jenis[i].title():<20}"
                    f"{jumlah_jenis[i]:>15}"
                )

            print("-" * 40)

            # Menentukan jenis cacat terbanyak
            terbesar = 0

            for i in range(1, len(jenis)):
                if jumlah_jenis[i] > jumlah_jenis[terbesar]:
                    terbesar = i

            print(
                "Jenis cacat terbanyak:",
                jenis[terbesar].title(),
                "-", jumlah_jenis[terbesar], "unit"
            )

            # 7. Tabel analisis per shift
            print("\nTABEL ANALISIS PER SHIFT")
            print("-" * 55)
            print(
                f"{'Shift':<12}"
                f"{'Produksi':>12}"
                f"{'Cacat':>12}"
                f"{'Tingkat (%)':>15}"
            )
            print("-" * 55)

            if produksi_A > 0:
                persen_A = cacat_A / produksi_A * 100
                print(
                    f"{'Shift A':<12}"
                    f"{produksi_A:>12}"
                    f"{cacat_A:>12}"
                    f"{round(persen_A, 2):>15}"
                )

            if produksi_B > 0:
                persen_B = cacat_B / produksi_B * 100
                print(
                    f"{'Shift B':<12}"
                    f"{produksi_B:>12}"
                    f"{cacat_B:>12}"
                    f"{round(persen_B, 2):>15}"
                )

            print("-" * 55)

        else:
            print("Tidak ada data valid untuk dianalisis")