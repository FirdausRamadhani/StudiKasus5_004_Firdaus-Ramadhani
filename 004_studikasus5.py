def hitung_parkir(jenis_parkir, durasi_parkir):
    if jenis_parkir.lower() == "mobil":
        tarif = 5000
    elif jenis_parkir.lower() == "motor":
        tarif = 3000
    else:
        tarif = 0

    biaya_parkir = tarif * durasi_parkir
    return biaya_parkir

jenis = input("Masukkan jenis parkir (mobil/motor) : ")
masuk = int(input("Masukkan jam masuk kendaraan (1-24): "))
keluar = int(input("Masukkan jam keluar kendaraan (1-24): "))

lama_parkir = keluar - masuk

hitung_parkir(jenis, lama_parkir)

print("\n======= Hasil Akhir Parkir =======")
print("Jenis Kendaraan     : ", jenis)
print("Jam Masuk           : ", masuk, "jam")
print("Jam Keluar          : ", keluar, "jam")
print("Lama Parkir         : ", lama_parkir,"jam")
print("Total Biaya Parkir  : RP",hitung_parkir(jenis, lama_parkir))
print("\n======== TERIMA KASIH ========")