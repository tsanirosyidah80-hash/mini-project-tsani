
import csv
import os
import statistics

FILE_CSV = "downtime_mesin.csv"

kolom_wajib = [
    "id_log",
    "id_mesin",
    "waktu_tersedia_menit",
    "downtime_menit",
    "kategori_gangguan",
    "tindakan_perbaikan"
]

data_valid = []
data_tidak_valid =[]

if not os.path.exists(FILE_CSV):
    print("ERROR: File CSV tidak ditemukan!")

else:
    try:
        with open(FILE_CSV, mode="r", encoding="utf-8-sig", newline="") as file:
          reader = csv.DictReader(file)

            
        if reader.fieldnames is None:
                print("ERROR: File CSV kosong atau tidak memiliki header!")

        elif not all(kolom in reader.fieldnames for kolom in kolom_wajib):
                print("ERROR: Kolom CSV tidak lengkap!")

        else:
                for nomor_baris, baris in enumerate(reader, start=2):
                    try:
                        
                        id_log = (baris["id_log"])
                        id_mesin = (baris["id_mesin"])
                        kategori = (baris["kategori_gangguan"])
                        tindakan = (baris["tindakan_perbaikan"])
                    
                        waktu_tersedia = int(
                            (baris["waktu_tersedia_menit"])
                        )
                        downtime = int(
                            (baris["downtime_menit"])
                        )

                        
                        if not all([
                            id_log,
                            id_mesin,
                            kategori,
                            tindakan
                        ]):
                            raise ValueError("Data teks kosong")

                        
                        waktu_tersedia = int(
                            (baris["waktu_tersedia_menit"])
                        )

                        downtime = int(
                            (baris["downtime_menit"])
                        )

                        
                        if waktu_tersedia <= 0:
                            raise ValueError("Waktu tersedia tidak valid")

                        if downtime < 0 or downtime > waktu_tersedia:
                            raise ValueError("Downtime tidak valid")

                        
                        waktu_operasi = waktu_tersedia - downtime

                        persentase_downtime = (downtime / waktu_tersedia )* 100

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
                        # Melewati data yang tidak valid
                        data_tidak_valid.append(baris)
                        
                        continue

                
                print("\n========== HASIL EVALUASI DOWNTIME MESIN ==========")

                if data_valid:

                    print("\nTABEL 1. HASIL PERHITUNGAN MESIN")

                    print("-" * 115)
                    print(
                        f"{'ID Log':<10}"
                        f"{'ID Mesin':<12}"
                        f"{'Tersedia':<13}"
                        f"{'Downtime':<12}"
                        f"{'Operasi':<12}"
                        f"{'Availability':<17}"
                        f"{'persentase downtime':<23}"
                        f"{'Status':<20}"
                    )
                    print("-" * 115)

                    for data in data_valid:
                        print(
                            f"{data['ID Log']:<10}"
                            f"{data['ID Mesin']:<12}"
                            f"{data['Waktu Tersedia']:<13}"
                            f"{data['Downtime']:<12}"
                            f"{data['Waktu Operasi']:<12}"
                            f"{data['Availability']:<17.2f}"
                            f"{persentase_downtime:<23.2f}"
                            f"{data['Status']:<20}"
                        )

                    print("-" * 115)

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

                    # Menghitung rata-rata availability
                    daftar_availability = [
                        data["Availability"] for data in data_valid
                    ]

                    rata_rata = statistics.mean(daftar_availability)

                    
                    print("\n========== RINGKASAN DATA ==========")

                    print("Jumlah Data Valid       :", len(data_valid))
                    print("Jumlah Data Tidak Valid :", len(data_tidak_valid))

                    print(
                        "Rata-rata Availability  : {:.2f}%".format(
                            rata_rata
                        )
                    )

                else:
                    print("\nTidak ada data valid untuk dievaluasi.")
                    print("Jumlah Data Valid       : 0")
                    print("Jumlah Data Tidak Valid :", len(data_tidak_valid))

    except (OSError, csv.Error, UnicodeError) as error:
        print("ERROR saat membaca file CSV:", error)
