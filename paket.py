from PKG.Modul1 import *
from PKG.Modul2 import *
from PKG.hitungnilai import hitung_nilai
from PKG.hitungnilai import jumlah_angka

def main():
    #memanggil fungsi fungsi dalam modul 1
    f1()
    f2()
    #memanggil fungsi fungsi dalam modul2
    F3()
    F4()
    print("Nilai_Akhir:",hitung_nilai(90,75))
    print("jumlah perkaian:",jumlah_angka(9,2))

main()
