def hitungGaji(golongan, lama):
    """
    Fungsi untuk menghitung gaji

    Parameter:
    golongan(string): jenis golongan pegawai, hanya terdapat 3 kemungkinan yaitu
    "I", "II", atau "III".
    lama(integer): lama masa kerja pegawai, harus berupa bilangan bulat non-negatif
    """
    if golongan == "I":
        return 1000000 + lama * 100000
    elif golongan == "II":
        return 3000000 + lama * 150000
    elif golongan == "III":
        return 5000000 + lama * 200000

# Program utama untuk meminta nilai yang valid dari user,
# dan hanya akan memanggil fungsi hitungGaji jika input sudah sesuai
# dengan spesifikasi fungsi hitungGaji

gol = ""
while not (gol == "I" or gol == "II" or gol == "III"):
    gol = input("Masukkan golongan: ")

input_ok = False
while not input_ok:
    try:
        lama = int(input("Masukkan lama kerja: "))
        if lama >= 0:
            input_ok = True
        else:
            print("Input tidak valid, lama kerja harus bilangan bulat non-negatif.")
    except ValueError:
        print("Input tidak valid, lama kerja harus bilangan bulat non-negatif.")

print("Gaji adalah", hitungGaji(gol, lama))
