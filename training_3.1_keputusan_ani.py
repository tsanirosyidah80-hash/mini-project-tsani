# Fungsi 1: Validasi input
def validasi_input(downtime, total_output, target_output, produk_cacat):
    if downtime < 0 or downtime > 10:
        return False
    if total_output <= 0 or target_output <= 0:
        return False
    if produk_cacat < 0 or produk_cacat > total_output:
        return False
    return True

# Fungsi 2: Menghitung Defect Rate
def hitung_defect_rate(produk_cacat, total_output):
    defect_rate = (produk_cacat / total_output) * 100
    return defect_rate

# Fungsi 3: Menghitung Skor
def hitung_skor(total_output, target_output, downtime, defect_rate):
    skor = ((total_output / target_output) * 70) \
           - (downtime * 5) \
           - (defect_rate * 2)

    return skor


# Fungsi 4: Klasifikasi kinerja
def klasifikasi_kinerja(downtime, defect_rate, skor):
    if downtime > 3 or defect_rate > 8:
        return "Bermasalah"
    elif skor >= 80:
        return "Kinerja Optimal"
    elif skor >= 50:
        return "Kinerja Standar"
    else:
        return "Kinerja Rendah"


# Program utama
print("=== EVALUASI KINERJA LINI PRODUKSI ===")

id_lini = input("Masukkan ID Lini: ")
waktu_berhenti = float(input("Masukkan Downtime (jam): "))
total_output = float(input("Masukkan Total Output (meter): "))
target_output = float(input("Masukkan Target Output (meter): "))
produk_cacat = float(input("Masukkan Jumlah Produk Cacat (meter): "))


# Validasi input
if validasi_input(waktu_berhenti, total_output, target_output, produk_cacat):

    # Perhitungan
    defect_rate = hitung_defect_rate(produk_cacat, total_output)

    skor = hitung_skor(total_output, target_output, waktu_berhenti, defect_rate )

    # Klasifikasi
    status = klasifikasi_kinerja(waktu_berhenti, defect_rate, skor)

    # Output
    print("\n=== HASIL EVALUASI ===")
    print("ID Lini       :", id_lini)
    print("Downtime      :", waktu_berhenti, "jam")
    print("Total Output  :", total_output, "meter")
    print("Target Output :", target_output, "meter")
    print("Produk Cacat  :", produk_cacat, "meter")
    print("Defect Rate   :", round(defect_rate, 2), "%")
    print("Skor          :", round(skor, 2))
    print("Klasifikasi   :", status)

else:
    print("\nInput tidak valid!")
    print("Periksa kembali data yang dimasukkan.")
