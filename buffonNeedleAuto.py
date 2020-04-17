import random
import numpy 
import time 

def main() :
    start = time.time()
    listNilai = []
    listError = []
    status = True
    iterasiNilai = 0
    while status :
        diameterPenampang = random.randint(0,1000)
        panjangNeedle = random.randint(0,1000)
        if(panjangNeedle > diameterPenampang ):
            print("Melanggar Peraturan L < D")
        else : 
            Q = 0
            i = 1
            banyakPercobaan = 1000
            while i <= banyakPercobaan: 
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
            if (Q == 0):
                nilaiPi = 0
            else :
                nilaiPi = (banyakPercobaan/Q)*((2.0*panjangNeedle)/diameterPenampang)
                error = abs(nilaiPi - 3.1415926535897932)
                listNilai.append(nilaiPi) 
                listError.append(error)
                iterasiNilai += 1
                if(round(nilaiPi,4) == 3.1415):
                    print(float("{:.4f}".format(nilaiPi)))
                    status = False
                else :
                    print(float("{:.4f}".format(nilaiPi))," ERROR VALUE: ",float(error))
            banyakPercobaan += 1000
    print('Waktu yang dibutuhkan : ',time.time()-start)

if __name__ == '__main__':
    main()


        