def hitung_umur(tahun_lahir):
    tahun_sekarang = 2026
    return tahun_sekarang - tahun_lahir

def tampilkan_biodata(nama, tahun):
    umur = hitung_umur(tahun)
    print(f"=== BIODATA ===")
    print(f"Nama  : {nama}")
    print(f"Umur  : {umur} tahun")
    print(f"Lahir : {tahun}")

nama = input("Nama kamu: ")

try:
    tahun = int(input("Tahun lahir: "))
    tampilkan_biodata(nama, tahun)
except ValueError:
    print("Error: Tahun lahir harus berupa angka!")
