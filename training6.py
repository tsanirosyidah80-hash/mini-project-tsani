import csv 
 jumlah_wo = 0 
 sesuai_rencana = 0 
 total_durasi = 0 
 
with open("maintenance_mesin_kelas_D.csv", "r") as file     
    reader = csv.DictReader(file) 
    
     for row in reader:        
         rencana = int(row["durasi_rencana"])        
         aktual = int(row["durasi_aktual"]) 
 
        selisih = aktual - rencana 
         if aktual <= rencana:            
             kondisi = "SESUAI"        
             else:            
             kondisi = "LEBIH LAMA" 
 
        print( 
            row["id_wo"],             row["mesin"],             aktual,             kondisi 
        ) 
 
        jumlah_wo += 1 
        total_durasi += aktual 
         if aktual <= rencana             sesuai_rencana += 1 
 print("\nRINGKASAN MAINTENANCE") print("Jumlah work order:", jumlah_wo) print("Sesuai rencana:", sesuai_rencana) 
print("Rata-rata durasi:", total_durasi / jumlah_wo 
