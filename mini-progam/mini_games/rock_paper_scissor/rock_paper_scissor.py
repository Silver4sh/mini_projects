from secrets import choice
import sys

def rock_paper_scissor():
    print("-----------------")
    print("Gunting Batu Kertas")
    print("-----------------")
    Seri = int()
    Kalah = int()
    Menang = int()
    Play = int(0)
    Menu1 = int(input("Main[1], Keluar[2] ? : "))
    while Menu1 == int(1):
        NumList = [0,1,2]
        List = ["Gunting","Batu","Kertas"]
        print("---------------")
        Menu2 = int(input("Main[1], Histori[2], Kembali[3] : "))
        while Menu2 == int(1):
            Player = input("Gunting, Batu, Kertas ? : ")
            Komputer = List[choice(NumList)]
            if Player == Komputer:
                print("---------------")
                print("Seri!")
                Play += 1
                Seri += 1
                Menu2 = 0
            elif Player == "Gunting":
                if Komputer == "Batu":
                    print("---------------")
                    print("Kamu Kalah!: Komputer memilih",Komputer)
                    Kalah += 1
                    Play += 1
                    Menu2 = 0
                else :
                    print("---------------")
                    print("Kamu Menang!: Komputer memilih",Komputer)
                    Play += 1
                    Menang += 1
                    Menu2 = 0
            elif Player == "Batu":
                if Komputer == "Gunting":
                    print("---------------")
                    print("Kamu Menang!: Komputer memilih",Komputer)
                    Play += 1
                    Menang += 1
                    Menu2 = 0
                else :
                    print("---------------")
                    print("Kamu Kalah!: Komputer memilih",Komputer)
                    Play += 1
                    Kalah += 1
                    Menu2 = 0
            elif Player == "Kertas":
                if Komputer == "Gunting":
                    print("---------------")
                    print("Kamu Kalah!: Komputer memilih",Komputer)
                    Play += 1
                    Kalah += 1
                    Menu2 = 0
                else :
                    print("---------------")
                    print("Kamu Menang!: Komputer memilih",Komputer)
                    Play += 1
                    Menang += 1
                    Menu2 = 0
            else :
                print("---------------")
                print("Pilihan yang kamu masukkan salah")
        while Menu2 == int(2):
            print("---------------")
            Menu3 = int(input("Lihat Histori[1], Hapus Histori[2], Kembali[3] : "))
            if Menu3 == 1:
                if Play == int(0):
                    print("---------------")
                    print("Anda belum bermain")
                    Menu2 = 0
                elif Play > int(0):
                    print("---------------")
                    print("Menang : %i" %Menang)
                    print("---------------")
                    print("Kalah : %i" %Kalah)
                    print("---------------")
                    print("Seri : %i" %Seri)
                    print("---------------")
                    print("Bermain : %i" %Play)
                    Winrate = Menang / Play
                    print("---------------")
                    print("Winrate : %i" %Winrate)
            elif Menu3 == 2:
                Menang = 0
                Kalah = 0
                Seri = 0
                Play = 0
            elif Menu3 == 3:
                Menu2 = 0
            else:
                print("---------------")
                print("Pilihan yang kamu masukkan salah")
        while Menu2 == int(3):
            sys.exit()
    while Menu1 == int(2):
        sys.exit()
rock_paper_scissor()