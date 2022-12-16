a = (1, 2, 3, 4, 10, 20, 30, 100, 200, 300, 400, 1000, 2000, 3000)
b = (3, 15, 5, 6, 8, 9, 11, 12, 13, 4, 200, 300)

def ABC(x1,x2):
    Irisan = []
    for i in range(0,len(x1)):
        x1_1 = x1[i]
        for j in range(len(x2)):
            if x1_1==x2[j]:
                Irisan.append(int(x1_1))
                j += 1
            i += 1
    print("Nilai yang kembar dari var1 dan var2 adalah :")
    print(Irisan)

ABC(a,b)