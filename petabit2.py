
#Muhamad Syarifudin - 5200411347
#Pandu Teja Sutrisno - 5200411343

import math

RAM = float(input("Masukkan Kapasitas RAM dalam MBps \n "))
BLOK = float(input("Masukkan Blok/Unit \n "))

print("\nKapasitas RAM \t\t\t: " + str(RAM) + " MBps.")
print("Blok/unit \t\t\t : " + str(BLOK) + " KBps.\n")
print("---------------------------------------------")
print("\nProgram Tereksekusi : ")

Alokasi0 = 0
Alokasi1 = 0
KPx = 0
i = 1
while i > 0:
    kapasPeta = float(input("\n Masukkan Program Tereksekusi (dalam KBps)\n (masukkan 0 jika tidak ada)\n "))

    if kapasPeta > 0:
        Alokasi1 += kapasPeta
        continue

    elif kapasPeta < 0:
        alokKP = math.fabs(kapasPeta)
        Alokasi0 += alokKP
        continue

    KPx += kapasPeta

    if KPx > 0 or KPx < 0:
        print("\n- Kapasitas Program " + str(i) + "\t\t: " + str(kapasPeta) + " KBps.")
        i += 1
        continue

    elif KPx == 0:
        TotalBlok = RAM / BLOK

        BlokNilai1 = KPx
        BlokNilai0 = TotalBlok - KPx

        print("\nInformasi kondisi peta bit :")
        print("Jumlah blok bernilai 1 \t\t  : " + str(int(kapasPeta)))
        print("Jumlah blok bernilai 0 \t\t  : " + str(int(BlokNilai0)))
        print("Alokasi blok bernilai 1 \t   : " + str(int(Alokasi1)))
        print("Alokasi blok bernilai 0 \t   : " + str(int(Alokasi0)))
        break

    else:
        print("input yang benar!")
        continue