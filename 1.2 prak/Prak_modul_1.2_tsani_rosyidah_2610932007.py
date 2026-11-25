nim = input("masukkan NIM : ")
A = int(nim [-1])
jumlah_produksi = A + 5


print("=================================")
print("==========TARGET PRODUKSI========")
print("JUMLAH PRODUKSI: ",jumlah_produksi)

if jumlah_produksi >= 100 :
    print("Target terpenuhi")
elif jumlah_produksi == 80 - 90 :
    print("Target hampir tercapai")
else :
    print("Target belum tercapai")



