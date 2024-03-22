#Atur cara mengira jumlah luas permukaan dan isipadu silinder
#Isytihar pemalar
pi=3.142

#Input
jejari=float(input("Masukkan jejari:"))
tinggi=float(input("Masukkan tinggi:"))

#Proses
jumlah_luas_permukaan=2*pi*(jejari**2)+2*pi*jejari*tinggi
isipadu=pi*(jejari**2)*tinggi

#Output
print("Jumlah luas permukaan bekas minuman ialah:",round(jumlah_luas_permukaan,2),"dan isipadu bekas minuman ialah:",round(isipadu,2))
