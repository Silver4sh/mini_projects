from secrets import choice
import sys

def rolling_dice():
    LemparDadu = int(input("Lempar Dadu[1], Keluar[2] : "))
    while LemparDadu == 1: 
        LemparDadu1 = int(input("Lempar [1], Keluar[2] :"))
        while LemparDadu1 == 1 :
            Dadu = int(input("Berapa banyak dadu yang ingin dilempar ? : "))
            Mata_Dadu = range(1,6)
            Result = []
            while Dadu != int(0):
                Try = choice(Mata_Dadu)
                Result.append(int(Try))
                Dadu -= 1
            print("---------")
            print(Result)
            print("---------")
            LemparDadu1 = 0
        while LemparDadu1 == 2:
            sys.exit()
    while LemparDadu == 2:
        sys.exit()
rolling_dice()