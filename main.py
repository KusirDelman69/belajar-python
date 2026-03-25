def hitung_umur(tahun_lahir):
    tahun_sekarang = 2026
    return tahun_sekarang - tahun_lahir

nama = input("Nama kamu: ")

try:
    tahun = int(input("Tahun lahir: "))
    print(f"Halo {nama}, umur kamu {hitung_umur(tahun)} tahun!")
except ValueError:
    print("Error: Tahun lahir harus berupa angka!")
