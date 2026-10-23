def konversi_menit_ke_detik(menit):
     """merubah menit menjadi detik.
    Parameter:
        menit (int/float): Jumlah menit yang akan diubah.
    Return:
        int/float: Jumlah detik hasil perubahan.
    """
     detik = menit * 60
     return detik
print(konversi_menit_ke_detik(3))
print(konversi_menit_ke_detik.__doc__)