import csv


data_valid = []
data_tidak_valid = []


try:
    with open("maintenance_mesin_kelas_D.csv", "r",encoding="utf-8-sig") as file:

        reader = csv.DictReader(file)

        for nomor, row in enumerate(reader, start=2):
            try:
                
                for key in row:
                    if key:
                        row[key] = (row[key] or "").strip()
                
                kolom_wajib = [
                    "tanggal", "id_wo", "mesin", "area",
                    "jenis_maintenance", "durasi_rencana",
                    "durasi_aktual", "downtime",
                    "status_pekerjaan"
                ]

                kosong = [
                    kolom for kolom in kolom_wajib
                    if not row.get(kolom)
                ]

                if kosong:
                    raise ValueError(
                        "Data kosong: " + ", ".join(kosong)
                    )
                
                rencana = int(row["durasi_rencana"])
                aktual = int(row["durasi_aktual"])
                downtime = int(row["downtime"])
                
                if rencana <= 0:
                    raise ValueError("Durasi rencana tidak valid")

                if aktual < 0 or downtime < 0:
                    raise ValueError("Durasi tidak boleh negatif")

                if rencana > 480 or aktual > 480:
                    raise ValueError("Durasi melebihi 480 menit")

                if downtime > aktual:
                    raise ValueError(
                        "Downtime melebihi durasi aktual"
                    )
                
                row["rencana"] = rencana
                row["aktual"] = aktual
                row["downtime_menit"] = downtime

                data_valid.append(row)

            except (ValueError, TypeError) as error:
                
                data_tidak_valid.append({
                    "baris": nomor,
                    "id_wo": row.get("id_wo", "Tidak diketahui"),
                    "alasan": str(error)
                })

except FileNotFoundError:
    print("File CSV tidak ditemukan.")

except Exception as error:
    print("Terjadi kesalahan:", error)

else:
    
    jumlah_corrective = {}

    for row in data_valid:

        if row["jenis_maintenance"].upper() == "CORRECTIVE":

            kunci = (row["tanggal"], row["mesin"])

            if kunci not in jumlah_corrective:
                jumlah_corrective[kunci] = 0

            jumlah_corrective[kunci] += 1
    
    hasil = []

    jumlah_selesai = 0
    jumlah_pending = 0
    terlambat = 0
    downtime_tinggi = 0
    total_durasi = 0

    for row in data_valid:

        rencana = row["rencana"]
        aktual = row["aktual"]
        downtime = row["downtime_menit"]

        status = row["status_pekerjaan"].upper()

        peringatan = []
        
        if status == "PENDING":
            jumlah_pending += 1
            peringatan.append("BELUM SELESAI")

        elif status == "SELESAI":
            jumlah_selesai += 1
            total_durasi += aktual
            
            if aktual > rencana * 1.20:
                peringatan.append("DURASI >20%")
                terlambat += 1
            
            if downtime > 60:
                peringatan.append("DOWNTIME >60 MENIT")
                downtime_tinggi += 1

        else:
            peringatan.append("STATUS TIDAK DIKENAL")
        
        kunci = (row["tanggal"], row["mesin"])

        if (row["jenis_maintenance"].upper() == "CORRECTIVE"
                and jumlah_corrective.get(kunci, 0) > 1):
            peringatan.append("CORRECTIVE BERULANG")

        if not peringatan:
            peringatan.append("NORMAL")

        hasil.append({
            "id": row["id_wo"],
            "mesin": row["mesin"],
            "status": status,
            "evaluasi": ", ".join(peringatan)
        })
    
    print("\n========== HASIL EVALUASI MAINTENANCE ==========")

    print(
        f"{'ID WO':<10} {'MESIN':<10} "
        f"{'STATUS':<12} {'HASIL EVALUASI'}"
    )

    print("-" * 75)

    for row in hasil:
        print(
            f"{row['id']:<10} "
            f"{row['mesin']:<10} "
            f"{row['status']:<12} "
            f"{row['evaluasi']}"
        )
    
    print("\n========== RINGKASAN MAINTENANCE ==========")

    print("Total data valid       :", len(data_valid))
    print("Total data tidak valid :", len(data_tidak_valid))
    print("Pekerjaan selesai      :", jumlah_selesai)
    print("Pekerjaan pending      :", jumlah_pending)
    print("Durasi lebih dari 20%  :", terlambat)
    print("Downtime lebih dari 60 :", downtime_tinggi)

    if jumlah_selesai > 0:
        rata_rata = total_durasi / jumlah_selesai
        print("Rata-rata durasi aktual:", round(rata_rata, 2), "menit")
    else:
        print("Rata-rata durasi aktual: Belum ada data selesai")
    
    print("\n========== DATA TIDAK VALID ==========")

    if len(data_tidak_valid) == 0:
        print("Tidak ada data yang tidak valid.")

    else:
        for data in data_tidak_valid:
            print(
                data["id_wo"],
                "| Baris:", data["baris"],
                "| Alasan:", data["alasan"]
            )

        print("Jumlah data tidak valid:", len(data_tidak_valid))