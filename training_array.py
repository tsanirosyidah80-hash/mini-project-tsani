import csv
import statistics

# Nama file CSV
FILE_CSV = "Downtime_mesin.csv"

# Struktur data
data_valid = []
data_tidak_valid = []

# Membaca file CSV
with open(FILE_CSV, mode="r", encoding="cp1252", newline="") as csv_file:

    reader = csv.DictReader(csv_file)

    # Memeriksa kolom CSV
    kolom_wajib = [
        "id_log",
        "id_mesin",
        "waktu_tersedia_menit",
        "downtime_menit",
        "kategori_gangguan",
        "tindakan_perbaikan"
    ]

    if not (kolom in reader.fieldnames for kolom in kolom_wajib):
        print("ERROR: Kolom CSV tidak lengkap!")

    else:

        # Validasi setiap baris
        for baris in reader:

            try:
                # Mengambil data
                id_log = baris["id_log"].strip()
                id_mesin = baris["id_mesin"].strip()
                kategori = baris["kategori_gangguan"].strip()
                tindakan = baris["tindakan_perbaikan"].strip()

                tersedia = int(baris["waktu_tersedia_menit"])
                downtime = int(baris["downtime_menit"])

                # Memeriksa data kosong
                if (id_log == "" or id_mesin == "" or
                    kategori == "" or tindakan == ""):

                    raise ValueError("Data tidak boleh kosong")

                # Memeriksa waktu tersedia
                if tersedia <= 0:
                    raise ValueError("Waktu tersedia harus lebih dari 0")

                # Memeriksa downtime
                if downtime < 0:
                    raise ValueError("Downtime tidak boleh negatif")

                if downtime > tersedia:
                    raise ValueError("Downtime melebihi waktu tersedia")

                # Memasukkan data ke dictionary
                data = {
                    "id_log": id_log,
                    "id_mesin": id_mesin,
                    "waktu_tersedia": tersedia,
                    "downtime": downtime,
                    "kategori": kategori,
                    "tindakan": tindakan
                }

                # Menyimpan ke list
                data_valid.append(data)

            except (ValueError, TypeError) as error:

                data_tidak_valid.append({
                    "id_log": baris.get("id_log", ""),
                    "alasan": str(error)
                })


# Menghitung evaluasi data valid
daftar_availability = []

print("\n===== HASIL EVALUASI DOWNTIME MESIN =====")

for data in data_valid:

    # Menghitung waktu operasi
    waktu_operasi = (
        data["waktu_tersedia"] - data["downtime"]
    )

    # Menghitung availability
    availability = (
        waktu_operasi / data["waktu_tersedia"]
    ) * 100

    daftar_availability.append(availability)

    # Menentukan status mesin
    if availability >= 95:
        status = "Sangat Baik"

    elif availability >= 90:
        status = "Baik"

    elif availability >= 85:
        status = "Cukup"

    else:
        status = "Perlu Perbaikan"

    # Menampilkan hasil
    print("\nID Log :", data["id_log"])
    print("ID Mesin :", data["id_mesin"])
    print("Kategori :", data["kategori"])
    print("Waktu Operasi :", waktu_operasi, "menit")
    print("Downtime :", data["downtime"], "menit")
    print("Availability :", round(availability, 2), "%")
    print("Status :", status)


# Menghitung rata-rata availability
if len(daftar_availability) > 0:

    rata_rata = statistics.mean(daftar_availability)

    print("\n===== RATA-RATA AVAILABILITY =====")
    print("Rata-rata :", round(rata_rata, 2), "%")

else:
    print("\nTidak ada data valid untuk dihitung.")


# Menampilkan jumlah data
print("\n===== REKAPITULASI DATA =====")

print("Jumlah data valid :", len(data_valid))
print("Jumlah data tidak valid :", len(data_tidak_valid))


# Menampilkan data tidak valid
print("\n===== DATA TIDAK VALID =====")

for data in data_tidak_valid:

    print("ID Log :", data["id_log"])
    print("Alasan :", data["alasan"])
    print("---------------------------")