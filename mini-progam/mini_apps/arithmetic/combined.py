a = (1, 2, 3, 4, 10, 20, 30, 100, 200, 300, 400, 1000, 2000, 3000)
b = (3, 15, 5, 6, 8, 9, 11, 12, 13, 4, 200, 300)

def ABC(x1,x2):
    Gabungan = []
    for i in range(0,len(x1)):
        x1_1=x1[i]
        Gabungan.append(int(x1_1))
        i += 1
    for j in range(len(x2)):
        x2_1=x2[j]
        Gabungan.append(int(x2_1))
        j += 1
    Gabungan = sorted(Gabungan)
    Gabungan_1 = list(dict.fromkeys(Gabungan))
    print("=====================================")
    print("Gabungan nilai dari var1 dan var2 adalah :")
    print(Gabungan)
    print("=====================================")
    print("Gabungan nilai dari var1 dan var2 dengan menghilangkan nilai ganda adalah :")
    print(Gabungan_1)

ABC(a,b)