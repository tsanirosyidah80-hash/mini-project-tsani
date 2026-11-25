import csv
import statistics

FILE_CSV = "downtime_mesin.csv"


kolom_wajib = [
    "ID Log",
    "ID Mesin",
    "Waktu Tersedia (menit)",
    "Downtime (menit)",
    "Kategori Gangguan",
    "Tindakan Perbaikan"
]

data_valid = []
jumlah_tidak_valid = 0

try:
    with open(FILE_CSV, mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        
        if reader.fieldnames is None or not all(
            kolom in reader.fieldnames for kolom in kolom_wajib
        ):
            print("ERROR: Kolom CSV tidak lengkap!")

        else:            
            for baris in reader:
                try:
                    id_log = baris["ID Log"].strip()
                    id_mesin = baris["ID Mesin"].strip()
                    kategori = baris["Kategori Gangguan"].strip()
                    tindakan = baris["Tindakan Perbaikan"].strip()

                    waktu_tersedia = int(baris["Waktu Tersedia (menit)"])

                    downtime = int(baris["Downtime (menit)"])
                    
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
                    
                    waktu_operasi = waktu_tersedia - downtime
                    
                    availability = (
                        waktu_operasi / waktu_tersedia
                    ) * 100
                    
                    if availability >= 95:
                        status = "Sangat Baik"
                    elif availability >= 90:
                        status = "Baik"
                    elif availability >= 85:
                        status = "Cukup"
                    else:
                        status = "Perlu Perbaikan"
                    
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

                except (ValueError, TypeError, KeyError, AttributeError):
                    jumlah_tidak_valid += 1
            
            print("\n========== HASIL EVALUASI DOWNTIME MESIN ==========")

            if data_valid:                
                print("\nTABEL 1. HASIL PERHITUNGAN MESIN")

                print("-" * 105)
                print(
                    f"{'ID Log':<10}"
                    f"{'ID Mesin':<12}"
                    f"{'Tersedia':<13}"
                    f"{'Downtime':<12}"
                    f"{'Operasi':<12}"
                    f"{'Availability':<17}"
                    f"{'Status':<20}"
                )
                print("-" * 105)

                for data in data_valid:
                    print(
                        f"{data['ID Log']:<10}"
                        f"{data['ID Mesin']:<12}"
                        f"{data['Waktu Tersedia']:<13}"
                        f"{data['Downtime']:<12}"
                        f"{data['Waktu Operasi']:<12}"
                        f"{data['Availability']:<17.2f}"
                        f"{data['Status']:<20}"
                    )

                print("-" * 105)
                
                print("\nTABEL 2. KATEGORI DAN TINDAKAN PERBAIKAN")

                print("-" * 80)
                print(
                    f"{'ID Log':<12}"
                    f"{'Kategori Gangguan':<25}"
                    f"{'Tindakan Perbaikan':<43}"
                )
                print("-" * 80)

                for data in data_valid:
                    print(
                        f"{data['ID Log']:<12}"
                        f"{data['Kategori']:<25}"
                        f"{data['Tindakan']:<43}"
                    )

                print("-" * 80)
                
                daftar_availability = [
                    data["Availability"] for data in data_valid
                ]

                rata_rata = statistics.mean(daftar_availability)
                
                print("\n========== RINGKASAN DATA ==========")

                print("Jumlah Data Valid       :", len(data_valid))
                print("Jumlah Data Tidak Valid :", jumlah_tidak_valid)
                print("Rata-rata Availability  : {:.2f}%".format(
                    rata_rata
                ))

            else:
                print("Tidak ada data valid untuk dievaluasi.")
                print("Jumlah Data Valid       : 0")
                print("Jumlah Data Tidak Valid :", jumlah_tidak_valid)

except FileNotFoundError:
    print("ERROR: File CSV tidak ditemukan!")