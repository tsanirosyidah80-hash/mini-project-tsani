nim = input("Masukkan NIM : ")
nama = input("Masukkan Nama : ")
kelompok = input("Masukkan Kelompok : ")
asisten = input("Masukkan Nama Asisten Pembimbing : ")
A =int(nim [-4])
B =int(nim[-3])
C = int(nim[-2])
D = int(nim[-1])
jumlah_bahan_baku = A + B
frekuensi = C + D
biaya_pemesanan_pokok = 40000
biaya_administrasi = 8.000
harga_bahan_baku = 12000
biaya_bongkar_muat = 1.500
biaya_asuransi_pengiriman = 0.04
total_biaya_pemesanan_pokok = biaya_pemesanan_pokok * frekuensi
total_biaya_administrasi = biaya_administrasi * frekuensi
total_harga_pembelian_bahan_baku = harga_bahan_baku * jumlah_bahan_baku
total_biaya_bongkar_muat = biaya_bongkar_muat * harga_bahan_baku
total_biaya_asuransi_pengiriman = biaya_asuransi_pengiriman * jumlah_bahan_baku
total_biaya_pengadaan_bahan_baku = total_biaya_pemesanan_pokok + total_biaya_administrasi + total_harga_pembelian_bahan_baku + total_biaya_bongkar_muat + total_biaya_asuransi_pengiriman

print("NIM :", nim)
print("Nama :", nama)
print("kelompok :", kelompok)
print("Asisten pembimbing :", asisten)
print("Bahan baku :", jumlah_bahan_baku)
print("Frekuensi :", frekuensi)
print("Biaya pemesanan pokok :", total_biaya_pemesanan_pokok)
print("Biaya administrasi :", total_biaya_administrasi)
print("Harga pembelian bahan baku :", total_harga_pembelian_bahan_baku)
print("biaya bongkar muat :", total_biaya_bongkar_muat)
print("biaya asuransi pengiriman :", total_biaya_asuransi_pengiriman)
print("Biaya pengadaan bahan baku secara keseluruhan :", total_biaya_pengadaan_bahan_baku)