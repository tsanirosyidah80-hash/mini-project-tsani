import csv

jumlah_wo = 0
sesuai_rencana = 0
terlambat = 0
total_durasi = 0
total_keterlambatan = 0
keterlambatan_terbesar = 0
mesin_terlambat = ""
data_tidak_valid = 0

id_wo_terdaftar = set()

with open("maintenance_mesin_kelas_D.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    # Validasi nama kolom CSV
    kolom_wajib = [
        "id_wo",
        "mesin",
        "durasi_rencana",
        "durasi_aktual"
    ]

    if not reader.fieldnames or not all(
        kolom in reader.fieldnames for kolom in kolom_wajib
    ):
        print("Error: Kolom CSV tidak lengkap.")
    else:

        for nomor, row in enumerate(reader, start=2):

            try:
                # Validasi data kosong
                if any(not row[kolom] or not row[kolom].strip()
                       for kolom in kolom_wajib):
                    raise ValueError("Data tidak boleh kosong")

                # Mengambil data
                id_wo = row["id_wo"].strip()
                mesin = row["mesin"].strip()

                # Validasi ID work order
                if id_wo in id_wo_terdaftar:
                    raise ValueError("ID work order duplikat")

                # Validasi tipe data
                rencana = int(row["durasi_rencana"])
                aktual = int(row["durasi_aktual"])

                # Validasi durasi
                if rencana <= 0 or aktual <= 0:
                    raise ValueError("Durasi harus lebih dari nol")

                # Menghitung selisih durasi
                selisih = aktual - rencana

                if aktual <= rencana:
                    kondisi = "SESUAI"
                else:
                    kondisi = "TERLAMBAT"

                # Menampilkan data yang valid
                print(
                    id_wo,
                    mesin,
                    rencana,
                    aktual,
                    selisih,
                    kondisi
                )

                id_wo_terdaftar.add(id_wo)

                jumlah_wo += 1
                total_durasi += aktual

                if aktual <= rencana:
                    sesuai_rencana += 1
                else:
                    terlambat += 1
                    total_keterlambatan += selisih

                    if selisih > keterlambatan_terbesar:
                        keterlambatan_terbesar = selisih
                        mesin_terlambat = mesin

            except ValueError as e:
                print("Baris", nomor, "tidak valid:", e)
                data_tidak_valid += 1

        # Evaluasi maintenance
        print("\nEVALUASI MAINTENANCE")

        print("Jumlah work order:", jumlah_wo)
        print("Data tidak valid:", data_tidak_valid)

        if jumlah_wo > 0:
            rata_rata = total_durasi / jumlah_wo

            print("Sesuai rencana:", sesuai_rencana)
            print("Terlambat:", terlambat)
            print("Rata-rata durasi:", round(rata_rata, 2))
            print("Total keterlambatan:", total_keterlambatan)

            if terlambat > 0:
                print("Keterlambatan terbesar:", keterlambatan_terbesar)
                print("Mesin yang perlu diperhatikan:", mesin_terlambat)
            else:
                print("Semua maintenance sesuai rencana.")

        else:
            print("Tidak ada data maintenance yang valid.")