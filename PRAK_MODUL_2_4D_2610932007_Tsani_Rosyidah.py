# MODUL 2 

def validasi_data_input (jumlah_operator,jam_kerja_efektif, total_output):
    while True:
        if jumlah_operator > 0:
          return True
        if 12 <= jam_kerja_efektif > 0:
            return True
        if total_output >= 0:
            return True
        else:
            return False

jumlah_lini_produksi= int(input("Masukkan jumlah lini produksi: "))
jumlah_operator= int(input("Masukkan jumlah operator: "))
jam_kerja_efektif= float(input("masukkan jam kerja efektif: "))
total_output= int(input("Masukkan total output: "))
target_produksi= int(input("Masukkan target produksi: "))
kapasitas_maksimum= int(input("Masukkan kapasitas maksimum: "))
    

def hitung_total_jam_tenaga_kerja (jumlah_operator, jam_kerja_efektif):
    total_jam_tenaga_kerja = jumlah_operator * jam_kerja_efektif
    return total_jam_tenaga_kerja

def hitung_produktivitas_tenaga_kerja (total_output, total_jam_tenaga_kerja):
    total_produktivitas_tenaga_kerja = total_output / total_jam_tenaga_kerja
    return total_produktivitas_tenaga_kerja

def hitung_total_output_per_operator (total_output, jumlah_operator):
    total_output_per_operator = total_output / jumlah_operator
    return total_output_per_operator

def hitung_total_persentase_pencapaian_target (total_output, target_produksi):
    total_persentase_pencapaian_target = (total_output/target_produksi)*100
    return total_persentase_pencapaian_target

def hitung_total_kekurangan_produksi (target_produksi, total_output):
    total_kekurangan_produksi = target_produksi - total_output
    return total_kekurangan_produksi

def hitung_total_utilisasi_kapasitas(total_output, kapasitas_maksimum):
    total_utilisasi_kapasitas = (total_output/kapasitas_maksimum)*100
    return total_utilisasi_kapasitas

def hitung_total_skor_produktivitas (persentase_pencapaian_target, utilisasi_kapasitas):
    total_skor_produktivitas = (persentase_pencapaian_target * 0.6) + (utilisasi_kapasitas * 0.4)
    return total_skor_produktivitas




def klasifikasi_status_lini_produksi(total_persentase_pencapaian_target, produktivitas_tenaga_kerja, total_skor_produktivitas):
    if total_persentase_pencapaian_target < 70: 
       print ("kinerja_rendah_atau_eveluasi_produksi")
    if produktivitas_tenaga_kerja < 5 :
        print ("kinerja_rendah_atau_eveluasi_produksi")
    if total_skor_produktivitas >= 85:
        print ("kinerja_baik")
    if 70<= total_skor_produktivitas < 85:
        print ("kinerja_normal")
    else:
        print ("kinerja_rendah")

print("============================================")
print("jumlah lini produksi: ", jumlah_lini_produksi)
print("jumlah operator: ",jumlah_operator)
print("jam kerja efektif: ", jam_kerja_efektif)
print("total output: ", total_output)
print("target produksi: ", target_produksi)
print("kapasitas maksimum: ", kapasitas_maksimum)





    