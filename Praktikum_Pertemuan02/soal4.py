total_detik = int(input("masukan detikk"))

jam = total_detik // 360
sisa_detik = total_detik % 360
menit = sisa_detik // 60
detik = sisa_detik % 60

print (f"{jam:02d}:{menit:02d}:{detik:02d}")