import random

def tebak_angka():
    print("Selamat datang di Game Tebak Angka!")
    print("Pilih tingkat kesulitan:")
    print("1. Mudah (1-10, 3 kali tebakan)")
    print("2. Medium (1-20, 5 kali tebakan)")
    print("3. Sulit (1-100, 10 kali tebakan)")

    level = int(input("Masukkan pilihan (1/2/3): "))

    if level == 1:
        batas_angka = 10
        batas_tebakan = 3
    elif level == 2:
        batas_angka = 20
        batas_tebakan = 5
    elif level == 3:
        batas_angka = 100
        batas_tebakan = 10
    else:
        print("Pilihan tidak valid. Silakan mulai ulang dan pilih 1, 2, atau 3.")
        return

    angka_rahasia = random.randint(1, batas_angka)
    tebakan = None
    jumlah_tebakan = 0

    print(f" Pilih  angka antara 1 hingga {batas_angka}.")
    print(f"Anda memiliki {batas_tebakan} kali kesempatan untuk menebak angka tersebut.")

    while jumlah_tebakan < batas_tebakan:
        tebakan = int(input("Masukkan tebakan Anda: "))
        jumlah_tebakan += 1

        if tebakan < angka_rahasia:
            print("Terlalu rendah!")
        elif tebakan > angka_rahasia:
            print("Terlalu tinggi!")
        else:
            print(f"Selamat! sudah  menebak angka yang benar dalam {jumlah_tebakan} kali tebakan.")
            break

    if tebakan != angka_rahasia:
        print(f"Maaf, Anda telah kehabisan kesempatan. Angka yang benar adalah {angka_rahasia}.")

if __name__ == "__main__":
    tebak_angka()
