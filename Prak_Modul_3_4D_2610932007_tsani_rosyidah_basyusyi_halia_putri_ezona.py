import csv
import statistik

FILE_CSV = r"Downtime_mesin.csv"

KOLOM_WAJIB = ["id_log", "id_mesin", "waktu_tersedia_menit", "downtime_menit", "kategori_gangguan", "tindakan_perbaikan"]

if not statistik.path.exists(FILE_CSV):
    print(f"Error: File CSV '{FILE_CSV}' tidak ditemukan.")
else:
    with open(FILE_CSV, "r",encoding="utf-8") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames is None:
            print("Error: Dataset tidak memiliki header.")
        elif not all(kolo\m in reader.fieldnames for kolom in KOLOM_WAJIB):
            kolom_hilang = [kolom for kolom in KOLOM_WAJIB if kolom not in reader.fieldnames]
            print("Error: Kolom berikut tidak ditemukan:")
            for kolom in kolom_hilang:
                print(f"-{kolom}")
        else:
            data = []
            for nomor_baris, row in enumerate(reader, start=2):
                try:
                    id_log = row["id_log"].strip()
                    id_mesin = row["id_mesin"].strip()
                    waktu_tersedia_menit = int(row["waktu_tersedia_menit"])
                    downtime_menit = int(row["downtime_menit"])
                    kategori_gangguan = row["kategori_gangguan"].strip()
                    tindakan_perbaikan = row["tindakan_perbaikan"].strip()

                    if waktu_tersedia_menit < 0 or downtime_menit < 0:
                        print(f"Peringatan baris {nomor_baris}: Nilai waktu tersedia/downtime tidak boleh nol atau negatif.")
                        continue
                    if downtime_menit > waktu_tersedia_menit:
                        print(f"Peringatan baris {nomor_baris}: Downtime ({downtime_menit}) tidak boleh melebihi waktu tersedia ({waktu_tersedia_menit}).")
                        continue

                    data.append({
                        "id_log": id_log,
                        "id_mesin": id_mesin,
                        "waktu_tersedia_menit": waktu_tersedia_menit,
                        "downtime_menit": downtime_menit,
                        "kategori_gangguan": kategori_gangguan,
                        "tindakan_perbaikan": tindakan_perbaikan
                    })

                except ValueError:
                    print(f"Peringatan baris {nomor_baris}: Salah satu nilai numerik (waktu tersedia/downtime) bukan bilangan bulat valid.")


if data:
    print("Data berhasil dibaca dan divalidasi:")
    for row in data:
     print(row)

                     