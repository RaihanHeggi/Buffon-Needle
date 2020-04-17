import random
import numpy 
import time 

def showPiValue(listNilaiPi,listError): 
    for i in range(0,len(listNilaiPi)):
        print("Nilai Pi = ",listNilaiPi[i],'Error Value =',listError[i])
    print("End Of Program")

def showPiCorrect(listNilaiAkhir,listNilaiPi,listError,listErrorAkhir,nilaiError): 
    if(len(listNilaiAkhir) > 0):
        for i in range(0,len(listNilaiAkhir)):           
            print("Nilai Pi = ",round(listNilaiAkhir[i],8)," Error Pada Nilai Akhir = ",str(nilaiError)," Error Value Keseluruhan Percobaan= ",listErrorAkhir[i])
        print("End Of Program")
    else : 
        print('Nilai Belum Ditemukan')
        pilih = str(input('Cek Nilai Pi (y/n) '))
        if(pilih == 'y'):
            showPiValue(listNilaiPi,listError)
        else : 
            main()


def isiPercobaan(n):
    listArrayNilai = []
    isi = 1
    for i in range(0,n) :
        listArrayNilai.append(isi)
        isi += 1
    return listArrayNilai

def main() :
    diameterPenampang = int(input("Masukkan Luas Diameter Penampang : "))
    panjangNeedle = int(input("Masukkan Panjang Needle yang di inginkan : "))
    batasPercobaan = int(input('Masukkan Batas nilai Percobaan yang di lakukan : '))
    nilaiError = 0
    if(panjangNeedle > diameterPenampang ):
        print("Melanggar Peraturan L < D")
    else : 
        Q = 0
        i = 1
        listNilaiPi = []
        listNilaiAkhir = []
        listError =[]
        listErrorAkhir = []
        cek = True
        banyakPercobaan = isiPercobaan(batasPercobaan)
        iterasiNilai = 1
        sumn = 0
        while cek:
            while i <= banyakPercobaan[iterasiNilai] : 
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
                iterasiNilai += 1
            else :
                nilaiPi = (banyakPercobaan[iterasiNilai]/Q)*((2*panjangNeedle)/diameterPenampang)
                if (float("{:.8f}".format(nilaiPi)) == 3.1415926535897932): 
                    nilaiError = abs(nilaiPi - 3.1415926535897932)
                    listNilaiAkhir.append(nilaiPi)
                    sumn += banyakPercobaan[iterasiNilai]/Q
                    iterasiNilai+= 1
                    error = abs(float((1/iterasiNilai)*(((2*panjangNeedle)/diameterPenampang))*sumn)-3.1415926535897932)
                    listErrorAkhir.append(error)
                    cek = False
                else :
                    listNilaiPi.append(nilaiPi)
                    sumn += banyakPercobaan[iterasiNilai]/Q
                    iterasiNilai+= 1
                    error = abs(float((1/iterasiNilai)*(((2*panjangNeedle)/diameterPenampang))*sumn)-3.1415926535897932)
                    listError.append(error)
                    if(iterasiNilai == len(banyakPercobaan)):
                        cek = False
    showPiCorrect(listNilaiAkhir,listNilaiPi,listError,listErrorAkhir,nilaiError)
    
if __name__ == '__main__':
    main()


        