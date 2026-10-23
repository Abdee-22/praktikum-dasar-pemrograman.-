soal = [ 
"Ibu kota Indonesia adalah?", 
"2 + 2 * 3 hasilnya adalah?", 
"Tipe data untuk teks pada Python disebut?", 
"Siapa juara MPL season 9?",
"Siapa Presiden Republik Indonesia Yang dijuluki Gemoy?"
] 
kunci = ["Jakarta", "8", "string", "KINK RRQ", "Prabroro"] 
skor = 0 
for nomor in range(len(soal)): 
    print(f"\nSoal {nomor + 1}: {soal[nomor]}") 
    jawaban = input("Jawaban Anda: ") 
    if jawaban.strip().lower() == kunci[nomor].lower(): 
        print("Benar!") 
        skor += 1 
    else: 
        print(f"Salah. Jawaban benar: {kunci[nomor]}") 
print(f"\nSkor akhir: {skor}/{len(soal)}") 
nilai = skor / len(soal) * 100
print (f"Nilai akhir: {nilai:.0f}")