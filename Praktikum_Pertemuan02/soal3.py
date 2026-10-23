harga_satuan = float(input("Masukkan harga satuan: "))
jumlah_barang = int(input("Masukkan jumlah barang: "))
persentase_diskon = float(input("Masukkan persentase diskon (contoh: 3 untuk 3%): "))

subtotal = harga_satuan * jumlah_barang
nominal_diskon = subtotal * (persentase_diskon / 100)
total_bayar = subtotal - nominal_diskon

print(f"Subtotal: Rp{subtotal}")
print(f"Nominal Diskon ({persentase_diskon}%): Rp{nominal_diskon}")
print(f"Total Bayar: Rp{total_bayar}")