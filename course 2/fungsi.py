#hitung luas segitiga
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas ={alas} dan tinggi ={tinggi} memiliki luas ={luas_segitiga}')

alas = 20
tinggi = 2
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas ={alas} dan tinggi ={tinggi} memiliki luas ={luas_segitiga}')

#fungsi
def hitung_luas(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

print(f"hasil: {hitung_luas(10, 6)}")
print(f"hasil: {hitung_luas(20, 2)}")