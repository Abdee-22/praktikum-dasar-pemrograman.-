#proogram Kalkulator Sederhana
print("=== Kalkulator Sederhana ===")
angka1 = float(input("masukan angka pertama: "))
operator = input("masukan opertaor (+,-,*,/):")
angka2 = float(input("Masukan Angka Kedua: "))

if operator == "+":
    hasil = angka1 + angka2
    print (int(hasil))
elif operator == "-":
    hasil = angka1 - angka2
    print (int(hasil))
elif operator == "*":
    hasil = angka1 * angka2
    print (int(hasil))
elif operator == "/":
    if angka2 !=0:
     hasil = angka1 / angka2
     print (int(hasil))
    else:
        print("error: Pembagian dengan nol tidak diperbolehkan")
    
elif operator == "%":
    hasil = angka1 % angka2
else:
    hasil = "Operator tidak dikenali"
    print ("Hasil", hasil )