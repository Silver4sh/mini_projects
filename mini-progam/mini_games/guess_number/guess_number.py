from random import choice
import sys

def guess_number():
    print("---------------")
    print("Tebak Angka")
    print("---------------")
    play = int(input("Do you want play a guess number ? : Yes[1] or No[2] : "))
    Menang = int(0)
    Kalah = int(0)
    Bermain = int(0)
    if play == int(1):
        while play == int(1):
            print("---------------")
            Menu_1 = int(input("Main[1], Histori[2], Keluar[3] : "))
            if Menu_1 == int(1):
                Kesempatan = 5
                Number = range(0,9)
                Komputer = str(choice(Number))
                while Menu_1 == int(1) :
                    print("---------------")
                    print("Kamu hanya memiliki 5 kesempatan menebak!")
                    while Kesempatan != 0:
                        tebakan = str(input("Masukkan nilai tebakan-mu dari 0-9: "))
                        if tebakan < Komputer:
                            print("---------------")
                            print("Tebakanmu terlalu kecil! \n coba lagi!")
                            Kesempatan -= 1
                        elif tebakan > Komputer:
                            print("---------------")
                            print("Tebakanmu terlalu besar! \n coba lagi!")
                            Kesempatan -= 1
                        elif tebakan == Komputer:
                            print("---------------")
                            print("Tebakanmu benar!!")
                            Menang += 1
                            Bermain += 1
                            Kesempatan = 0
                        else :
                            print("---------------")
                            print("Kesempatanmu Habis!")
                            print("Kamu Kalah!")
                            Kalah += 1
                    Menu_1 = 0
            elif Menu_1 == int(2):
                print("---------------")
                Menu_2 = str(input("Lihat Histori [1], Bersihkan Histori[2] : "))
                if Menu_2 == str(1):
                    if Bermain > 0:
                        print("---------------")
                        print("Menang : %i" %Menang)
                        print("Kalah : %i" %Kalah)
                        print("---------------")
                        print("Bermain : %i" %Bermain)
                        Winrate = Menang / Bermain
                        print("Winrate : %i" %Winrate )
                    else :
                        print("---------------")
                        print("Anda belum bermain!")
                elif Menu_2 == str(2):
                    Menang = int()
                    Kalah = int()
                    Bermain = int()
                else :
                    print("---------------")
                    print("Nilai yang anda input salah!")
            elif Menu_1 == int(3):
                print("---------------")
                print("Terimakasih Telah Bermain \n Sampai Jumpa Lagi!!")
                sys.exit()
            else:
                print("---------------")
                print("Nilai yang anda input salah!")
    elif play == int(2) :
        print("---------------")
        print("Terimakasih Telah Bermain \n Sampai Jumpa Lagi!!")
        sys.exit()
    else:
        print("Nilai yang anda input salah!")
guess_number()