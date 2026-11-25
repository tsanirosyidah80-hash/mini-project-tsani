jumlah_kendaraan = 0
total_pendapatan = 0

while True:
    print("==== DATA PARKIR ====")

    lama_parkir = int(input("Masukkan lama parkir (jam): "))

    if 1 <= lama_parkir <= 2 :
        biaya = 5000
    elif 3 <= lama_parkir <=5 :
        biaya = 10000
    elif lama_parkir > 5 :
        biaya = 15000
    
    else:
        print("EROR")
        continue

    jumlah_kendaraan += 1
    total_pendapatan += biaya

    print("Biaya parkir: Rp", biaya)

    ada_kendaraan_lagi = input("apakah ada kendaraan lagi? (y/n): ")
    if ada_kendaraan_lagi == "n" :
        break

    print("==================================")
    print("========== HASIL PARKIR ==========")
    print("jumlah seluruh kendaraan :", jumlah_kendaraan)
    print("Total pendapatan : Rp", total_pendapatan)
