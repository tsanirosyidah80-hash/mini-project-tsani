import csv
import statistics

# 1. Menentukan nama file CSV
FILE_CSV = "downtime_mesin.csv"

# 2. Menentukan kolom yang wajib tersedia
kolom_wajib = [
    "ID Log",
    "ID Mesin",
    "Waktu Tersedia (menit)",
    "Downtime (menit)",
    "Kategori Gangguan",
    "Tindakan Perbaikan"
]

# 3. Menyiapkan list untuk menyimpan data
data_valid = []
jumlah_tidak_valid = 0

# 4. Membaca file CSV
try:
    with open(FILE_CSV, mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        # 5. Memeriksa kelengkapan kolom
        if reader.fieldnames is None or not all(
            kolom in reader.fieldnames for kolom in kolom_wajib
        ):
            print("ERROR: Kolom CSV tidak lengkap!")

        else:
            # 6. Memeriksa setiap baris data
            for baris in reader:

                try:
                    id_log = baris["ID Log"].strip()
                    id_mesin = baris["ID Mesin"].strip()
                    kategori = baris["Kategori Gangguan"].strip()
                    tindakan = baris["Tindakan Perbaikan"].strip()

                    waktu_tersedia = int(
                        baris["Waktu Tersedia (menit)"]
                    )

                    downtime = int(
                        baris["Downtime (menit)"]
                    )

                    # 7. Validasi data
                    if (
                        id_log == ""
                        or id_mesin == ""
                        or kategori == ""
                        or tindakan == ""
                        or waktu_tersedia <= 0
                        or downtime < 0
                        or downtime > waktu_tersedia
                    ):
                        jumlah_tidak_valid += 1
                        continue

                    # 8. Menghitung waktu operasi
                    waktu_operasi = waktu_tersedia - downtime

                    # 9. Menghitung availability
                    availability = (
                        waktu_operasi / waktu_tersedia
                    ) * 100

                    # 10. Menentukan status mesin
                    if availability >= 95:
                        status = "Sangat Baik"
                    elif availability >= 90:
                        status = "Baik"
                    elif availability >= 85:
                        status = "Cukup"
                    else:
                        status = "Perlu Perbaikan"

                    # 11. Menyimpan data ke list of dictionary
                    data_valid.append({
                        "ID Log": id_log,
                        "ID Mesin": id_mesin,
                        "Waktu Tersedia": waktu_tersedia,
                        "Downtime": downtime,
                        "Waktu Operasi": waktu_operasi,
                        "Availability": availability,
                        "Kategori": kategori,
                        "Tindakan": tindakan,
                        "Status": status
                    })

                except (ValueError, TypeError, KeyError):
                    jumlah_tidak_valid += 1

            # 12. Menampilkan hasil evaluasi
            if data_valid:
                print("\n===== HASIL EVALUASI DOWNTIME MESIN =====")

                for data in data_valid:
                    print("\nID Log          :", data["ID Log"])
                    print("ID Mesin        :", data["ID Mesin"])
                    print("Waktu Tersedia  :", data["Waktu Tersedia"])
                    print("Downtime        :", data["Downtime"])
                    print("Waktu Operasi   :", data["Waktu Operasi"])
                    print("Availability    : {:.2f}%".format(
                        data["Availability"]
                    ))
                    print("Kategori        :", data["Kategori"])
                    print("Tindakan        :", data["Tindakan"])
                    print("Status Mesin    :", data["Status"])

                # 13. Menghitung rata-rata availability
                daftar_availability = [
                    data["Availability"] for data in data_valid
                ]

                rata_rata = statistics.mean(daftar_availability)

                print("\n===== RINGKASAN DATA =====")
                print("Jumlah Data Valid       :", len(data_valid))
                print("Jumlah Data Tidak Valid :", jumlah_tidak_valid)
                print("Rata-rata Availability  : {:.2f}%".format(
                    rata_rata
                ))

            else:
                print("Tidak ada data valid untuk dievaluasi.")
                print("Jumlah Data Valid       :", 0)
                print("Jumlah Data Tidak Valid :", jumlah_tidak_valid)

except FileNotFoundError:
    print("ERROR: File CSV tidak ditemukan!")