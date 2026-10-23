def hitung_subtotal(harga, jumlah):
    return harga * jumlah

def hitung_diskon(subtotal):
    if subtotal>=10000:
        return int (subtotal*0.10)
    return 
    
def tampilkan_struk(nama_barang, subtotal, diskon ):
    total_akhir= subtotal - diskon
    print("===print struk===")
    print(f"Nama Barang: {nama_barang}")
    print(f"Subtotal: {subtotal}")
    print(f"Diskon : {diskon}")
    print(f"Total akhir : {total_akhir}")

#program utama
nama_barang= "buku"
harga = 25000
jumlah = 5

subtotal= hitung_subtotal(harga, jumlah)
diskon= hitung_diskon(subtotal)
tampilkan_struk(nama_barang, subtotal, diskon)