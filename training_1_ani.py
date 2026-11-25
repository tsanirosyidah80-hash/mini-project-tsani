# PROGRAM PERHITUNGAN BIAYA PEMESANAN BAHAN BAKU

# 1. Input Data Mahasiswa
nim = input("Masukkan NIM: ")
nama = input("Masukkan Nama: ")
kelompok = input("Masukkan Kelompok: ")
asisten = input("Masukkan Asisten Pembimbing: ")

# 2. Mengambil 4 Digit Terakhir NIM
A = int(nim[-4])
B = int(nim[-3])
C = int(nim[-2])
D = int(nim[-1])

# 3. menghuitung jumlah bahan baku dan frekuensi pemasaran
jumlah_bahan = A + B
frekuensi = C + D

# 4. menentukan biaya
biaya_pemesanan_pokok = 50000
biaya_administrasi = 10000
harga_bahan = 15000
biaya_bongkar = 2000
persen_asuransi = 0.05

# 5. menghitung biaya pemesanan pokok
total_pemesanan_pokok = biaya_pemesanan_pokok * frekuensi
# 6. mengitung biaya administrasi
total_administrasi = biaya_administrasi * frekuensi
# 7. menghitung harga bahan baku
total_harga_bahan = harga_bahan * frekuensi
# 8. menghitung biaya bongkar muat 
total_bongkar = biaya_bongkar * jumlah_bahan
# 9. menghitung biaya asuransi pengiriman 
total_asuransi = persen_asuransi * total_harga_bahan
total_keseluruhan = (total_pemesanan_pokok + total_administrasi + total_harga_bahan + total_bongkar + total_asuransi)

print("\n===========================")
print("       HASIL PERHITUNGAN BIAYA")
print("==============================")

print("NIM     :", nim)
print("Nama    :", nama)
print("Kelompok :", kelompok)
print("Asisten Pembimbing :", asisten)
print("---------------------------------------------------")
print("Jumlah bahan baku :", jumlah_bahan, "unit")
print("Frekuensi         :", frekuensi)
print("Biaya pemesanan pokok  : Rp", total_pemesanan_pokok)
print("Biaya administrasi     : Rp", total_administrasi)
print("Harga bahan            : Rp", total_harga_bahan)
print("Biaya bongkar          : Rp", total_bongkar)
print("Persen asuransi        : RP", total_asuransi)
print("-----------------------------------------------------")
print("Biaya keseluruhan      : Rp", total_keseluruhan)
print("-----------------------------------------------------")
