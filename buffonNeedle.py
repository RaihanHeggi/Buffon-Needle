import random
import numpy 
import time 

start = time.time()
banyakPercobaan = int(input("Masukkan Banyaknya Needle yang dimiliki : "))
diameterPenampang = int(input("Masukkan Luas Diameter Penampang :"))
panjangNeedle = int(input("Masukkan Panjang Needle yang di inginkan :"))

if(panjangNeedle > diameterPenampang ):
    print("Melanggar Peraturan L < D")
else : 
    Q = 0
    i = 1
    while i <= banyakPercobaan : 
        xi = random.uniform(0,diameterPenampang)
        yi = random.randint(0,90)     
        if xi < (panjangNeedle*numpy.cos(numpy.deg2rad(yi))) :
            Q += 1
            i += 1
            if i == banyakPercobaan :
                break 
        else : 
            Q += 0
            i += 1  
            if i == banyakPercobaan :
                break 
    nilaiPi = (banyakPercobaan/Q)*((2*panjangNeedle)/diameterPenampang)
    print("Nilai Pi = ",nilaiPi)
    print("Time ",time.time() - start)