import sys
print("====================")
print("Converter Suhu")
print("====================")
Menu1 = int(input("Masuk[1], Keluar[2] : "))
print("====================")
while Menu1 == 1 :
    print("====================")
    Menu2 = int(input("Convert Suhu[1], Keluar[2] : "))
    print("====================")
    while Menu2 == 1:
        suhu = str(input("Jenis awal suhu : Celcius[1], Reamur[2], Fahrenheit[3], Kelvin[4] : "))
        if suhu == str(1):
            nilai1 = float(input("Masukkan nilai suhu : "))
            R1 = (5/4)* nilai1
            F1 = (9/5) * nilai1 + 32
            K1 = nilai1 + 273
            print("====================")
            print("Converter",nilai1,"C ke suhu Celcius adalah", nilai1,"C")
            print("Converter",nilai1,"C ke suhu Reamur adalah", R1,"R")
            print("Converter",nilai1,"C ke suhu Fahrenheit adalah", F1,"F")
            print("Converter",nilai1,"C ke suhu Kelvin adalah", K1,"K")
            print("====================")
            Menu2 = 0
        elif suhu == str(2):
            nilai1 = float(input("Masukkan nilai suhu : "))
            C2 = (5/4)*nilai1
            F2 = (9/4)*nilai1 + 32
            K2 = (5/4)*nilai1 + 273
            print("====================")
            print("Converter",nilai1,"R ke suhu Celcius adalah", C2,"C")
            print("Converter",nilai1,"R ke suhu Reamur adalah", nilai1,"R")
            print("Converter",nilai1,"R ke suhu Fahrenheit adalah", F2,"F")
            print("Converter",nilai1,"R ke suhu Kelvin adalah", K2,"K")
            print("====================")
            Menu2 = 0
        elif suhu == str(3):
            nilai1 = float(input("Masukkan nilai suhu : "))
            C3 = (5/9)*(nilai1-32)
            R3 = (4/5)*(nilai1-32)
            K3 = (5/9)*(nilai1-32)+273
            print("====================")
            print("Converter",nilai1,"F ke suhu Celcius adalah", C3,"C")
            print("Converter",nilai1,"F ke suhu Reamur adalah", R3,"R")
            print("Converter",nilai1,"F ke suhu Fahrenheit adalah", nilai1,"F")
            print("Converter",nilai1,"F ke suhu Kelvin adalah", K3,"K")
            print("====================")
            Menu2 = 0
        elif suhu == str(4):
            nilai1 = float(input("Masukkan nilai suhu : "))
            C4 = nilai1-273
            R4 = (4/5)*(nilai1-273)
            F4 = (9/5)*(nilai1-273)+32
            print("====================")
            print("Converter",nilai1,"K ke suhu Celcius adalah", C4,"C")
            print("Converter",nilai1,"K ke suhu Reamur adalah", R4,"R")
            print("Converter",nilai1,"K ke suhu Fahrenheit adalah", F4,"F")
            print("Converter",nilai1,"K ke suhu Kelvin adalah", nilai1,"K")
            print("====================")
            Menu2 = 0
        else :
            print("====================")
            print("Nilai yang anda masukkan salah")
            print("====================")
    while Menu2 == 2:
        sys.exit()
while Menu1 == 2:
    sys.exit()
