import sys
print("++++++++++++++++++++++")
print("Converter Jarak")
Menu1 = int(input("Masuk[1] , Keluar[2] : "))
while Menu1 == 1:
    Menu2 = int(input("Import Jarak[1] , Keluar[2] : "))
    while Menu2 == 1:
        jarak = int(input("Masukkan jarak awal : \"KM[1], HM[2], DAM[3], M[4], DM[5], CM[6], MM[7] : "))
        nilai = float(input("Masukkan nilai jarak : "))
        if jarak == 1:
            km = nilai
            hm = 10 * km
            dam = 10 * hm
            m = 10 * dam
            dm = 10 * m
            cm = 10 * dm
            mm = 10 * cm
            print("----------------------------")
            print("Converter %.9f"%nilai,"km ke km adalah %.9f" %km,"km")
            print("Converter %.9f"%nilai,"km ke hm adalah %.9f" %hm,"hm")
            print("Converter %.9f"%nilai,"km ke dam adalah %.9f" %dam,"dam")
            print("Converter %.9f"%nilai,"km ke m adalah %.9f" %m,"m")
            print("Converter %.9f"%nilai,"km ke dm adalah %.9f" %dm,"dm")
            print("Converter %.9f"%nilai,"km ke cm adalah %.9f" %cm,"cm")
            print("Converter %.9f"%nilai,"km ke mm adalah %.9f" %mm,"mm")
            print("----------------------------")
            Menu2 = 0
        elif jarak == 2:
            hm = nilai
            km = .1 * hm
            dam = 10 * hm
            m = 10 * dam
            dm = 10 * m
            cm = 10 * dm
            mm = 10 * cm
            print("----------------------------")
            print("Converter %.9f"%nilai,"hm ke km adalah %.9f" %km,"km")
            print("Converter %.9f"%nilai,"hm ke hm adalah %.9f" %hm,"hm")
            print("Converter %.9f"%nilai,"hm ke dam adalah %.9f" %dam,"dam")
            print("Converter %.9f"%nilai,"hm ke m adalah %.9f" %m,"m")
            print("Converter %.9f"%nilai,"hm ke dm adalah %.9f" %dm,"dm")
            print("Converter %.9f"%nilai,"hm ke cm adalah %.9f" %cm,"cm")
            print("Converter %.9f"%nilai,"hm ke mm adalah %.9f" %mm,"mm")
            print("----------------------------")
            Menu2 = 0
        elif jarak == 3:
            dam = nilai
            hm = .1 * dam
            km = .1 * hm
            m = 10 * dam
            dm = 10 * m
            cm = 10 * dm
            mm = 10 * cm
            print("----------------------------")
            print("Converter %.9f"%nilai,"dam ke km adalah %.9f" %km,"km")
            print("Converter %.9f"%nilai,"dam ke hm adalah %.9f" %hm,"hm")
            print("Converter %.9f"%nilai,"dam ke dam adalah %.9f" %dam,"dam")
            print("Converter %.9f"%nilai,"dam ke m adalah %.9f" %m,"m")
            print("Converter %.9f"%nilai,"dam ke dm adalah %.9f" %dm,"dm")
            print("Converter %.9f"%nilai,"dam ke cm adalah %.9f" %cm,"cm")
            print("Converter %.9f"%nilai,"dam ke mm adalah %.9f" %mm,"mm")
            print("----------------------------")
            Menu2 = 0
        elif jarak == 4:
            m = nilai
            dam = .1 * m
            hm = .1 * dam
            km = .1 * hm
            dm = 10 * m
            cm = 10 * dm
            mm = 10 * cm
            print("----------------------------")
            print("Converter %.9f"%nilai,"m ke km adalah %.9f" %km,"km")
            print("Converter %.9f"%nilai,"m ke hm adalah %.9f" %hm,"hm")
            print("Converter %.9f"%nilai,"m ke dam adalah %.9f" %dam,"dam")
            print("Converter %.9f"%nilai,"m ke m adalah %.9f" %m,"m")
            print("Converter %.9f"%nilai,"m ke dm adalah %.9f" %dm,"dm")
            print("Converter %.9f"%nilai,"m ke cm adalah %.9f" %cm,"cm")
            print("Converter %.9f"%nilai,"m ke mm adalah %.9f" %mm,"mm")
            print("----------------------------")
            Menu2 = 0
        elif jarak == 5:
            dm = nilai
            m = .1 * dm
            dam = .1 * m
            hm = .1 * dam
            km = .1 * hm
            cm = 10 * dm
            mm = 10 * cm
            print("----------------------------")
            print("Converter %.9f"%nilai,"dm ke km adalah %.9f" %km,"km")
            print("Converter %.9f"%nilai,"m ke hm adalah %.9f" %hm,"hm")
            print("Converter %.9f"%nilai,"dm ke dam adalah %.9f" %dam,"dam")
            print("Converter %.9f"%nilai,"dm ke m adalah %.9f" %m,"m")
            print("Converter %.9f"%nilai,"dm ke dm adalah %.9f" %dm,"dm")
            print("Converter %.9f"%nilai,"dm ke cm adalah %.9f" %cm,"cm")
            print("Converter %.9f"%nilai,"dm ke mm adalah %.9f" %mm,"mm")
            print("----------------------------")
            Menu2 = 0
        elif jarak == 6:
            cm = nilai
            dm = .1 * cm
            m = .1 * dm
            dam = .1 * m
            hm = .1 * dam
            km = .1 * hm
            mm = 10 * cm
            print("----------------------------")
            print("Converter %.9f"%nilai,"cm ke km adalah %.9f" %km,"km")
            print("Converter %.9f"%nilai,"cm ke hm adalah %.9f" %hm,"hm")
            print("Converter %.9f"%nilai,"cm ke dam adalah %.9f" %dam,"dam")
            print("Converter %.9f"%nilai,"cm ke m adalah %.9f" %m,"m")
            print("Converter %.9f"%nilai,"cm ke dm adalah %.9f" %dm,"dm")
            print("Converter %.9f"%nilai,"cm ke cm adalah %.9f" %cm,"cm")
            print("Converter %.9f"%nilai,"cm ke mm adalah %.9f" %mm,"mm")
            print("----------------------------")
            Menu2 = 0
        elif jarak == 7:
            mm = nilai
            cm = .1 * mm
            dm = .1 * cm
            m = .1 * dm
            dam = .1 * m
            hm = .1 * dam
            km = .1 * hm
            print("----------------------------")
            print("Converter %.9f"%nilai,"mm ke km adalah %.9f" %km,"km")
            print("Converter %.9f"%nilai,"mm ke hm adalah %.9f" %hm,"hm")
            print("Converter %.9f"%nilai,"mm ke dam adalah %.9f" %dam,"dam")
            print("Converter %.9f"%nilai,"mm ke m adalah %.9f" %m,"m")
            print("Converter %.9f"%nilai,"mm ke dm adalah %.9f" %dm,"dm")
            print("Converter %.9f"%nilai,"mm ke cm adalah %.9f" %cm,"cm")
            print("Converter %.9f"%nilai,"mm ke mm adalah %.9f" %mm,"mm")
            print("----------------------------")
            Menu2 = 0
        else :
            print("Nilai yang anda masukkan salah")
    while Menu2 == 2:
        sys.exit()
while Menu1 == 2:
    sys.exit()
