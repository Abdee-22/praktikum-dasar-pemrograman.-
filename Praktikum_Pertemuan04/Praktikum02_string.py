kalimat = input("masukan Sebuah kalimat: ")
hitung_vokal = 0

for huruf in kalimat.lower():
    if huruf in "aiueo" :
        hitung_vokal += 1

print("jumlah huruf vokal:", hitung_vokal)