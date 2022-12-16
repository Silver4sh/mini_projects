import sys
Menu = int(input("Identifikasi bilangan (Masuk[1] Keluar[2]) : "))
while Menu == 1:
    Iden = int(input("Identifiksi bilangan (Ya[1], Tidak[2]) : "))
    while Iden == 1:
        Angka = int(input("Masukkan Bilangan: "))
        if Angka==0:
            print("%i Adalah Bilangan Netral" %Angka)
        elif Angka%2==0:
            print("%i Adalah Bilangan Genap" %Angka)
        else :
            print("%i Adalah Bilangan Ganjil" %Angka)
        Iden = 0
    while Iden == 2:
        sys.exit()
while Menu == 2:
    sys.exit()