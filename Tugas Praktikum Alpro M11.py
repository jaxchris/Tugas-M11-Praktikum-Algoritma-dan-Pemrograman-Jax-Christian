#Tugas Latihan Alpro Praktikum M12 Jax Christian 049 Kelas C
#Nomor 1
def cetak_garis():
    print("=" * 40)

cetak_garis()
cetak_garis()
#Nomor 2
def hitung_luas_persegi(sisi):
    luas = sisi * sisi
    print(f"Luas persegi adalah: {luas}")

hitung_luas_persegi(5)
hitung_luas_persegi(10)
hitung_luas_persegi(15)
#Nomor 3
def cek_genap(angka):
    if angka % 2 == 0:
        return True
    else:
        return False
status_angka = cek_genap(10)
print(status_angka)
#Nomor 3.1
def hitung_luas_persegi(sisi):
    luas = sisi * sisi
    print(f"Luas persegi adalah: {luas}")
    return luas 

def hitung_rata_rata(daftar_luas):
    return sum(daftar_luas) / len(daftar_luas)

luas1 = hitung_luas_persegi(5)
luas2 = hitung_luas_persegi(10)
luas3 = hitung_luas_persegi(15)

rata_rata = hitung_rata_rata([luas1, luas2, luas3])
print(f"Rata-rata luas persegi adalah: {rata_rata:.2f}")
#Nomor 4
def salam(waktu,nama="Kawan"):
    x=f"Selamat {waktu}, {nama}!"
    print(x)
    return x

salam("Pagi","Andi")
salam("Sore")
#Nomor 5
def konversi_nilai(nilai_angka):
    if nilai_angka >=86:
        return "A"
    elif nilai_angka >= 76 and nilai_angka <86:
        return "AB"
    elif nilai_angka >= 66 and nilai_angka <76:
        return "B"
    else:
        return "C"

a=int(input("Masukkan nilai angka: "))
konversi=konversi_nilai(a)
print(f"Nilai huruf Anda adalah: {konversi}")
