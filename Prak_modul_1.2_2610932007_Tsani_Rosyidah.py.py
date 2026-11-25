nim = input("Masukkan NIM: ")

A = int(nim[-1])
jumlah_proses = A + 5

print("==================================================")
print("     PROGRAM PENCAPAIN PRODUKSI ROLLER CHAIN      ")
print("==================================================")
print("NIM :", nim)
print("jumlah proses :", jumlah_proses)
print("==================================================")

for i in range(1, jumlah_proses + 1):
    print("proses produksi ke-", i)
    target = float(input("Masukkan target produksi : "))
    hasil = float(input("Masukkan hasil produksi : "))
    persentase = (hasil / target) * 100

    if persentase >= 100 :
        keterangan = "TARGET TERCAPAI"
    elif 99 >= persentase >= 80 :
        keterangan = "TARGET HAMPIR TERCAPAI"
    else :
        keterangan = "TARGET BELUM TERCAPAI"
    print("persentase pencapaian :", round(persentase, 2), "%")
    print("keterangan : ", keterangan)
    print("===============================================================")

print("=================================================================")
print("========================PEMERIKSAAN SELESAI======================")
print("=================================================================")
