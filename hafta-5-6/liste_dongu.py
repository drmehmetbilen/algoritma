"""
Rastgele 100 sayı üretilmesi.
Bu üretilen sayıların istatistiksel hesaplamaları. 
"""

import random

liste_eleman_sayisi = 11
r_alt_aralik = 0
r_ust_aralik = 100

# Rastgele Sayı Üretimi
sayilar = []
while len(sayilar)<liste_eleman_sayisi:
    yeni_sayi = random.randint(r_alt_aralik,r_ust_aralik)
    if yeni_sayi not in sayilar:
        sayilar.append(yeni_sayi)

# İstatistiksel Hesaplamalar
toplam = 0
for i in sayilar:
    toplam = toplam + i

print(sayilar)
print("Liste eleman sayısı :", len(sayilar))
print("Sayıların Toplamı : ",toplam)
print("Sayıların Ortalaması :", toplam/len(sayilar))

# En büyük (max)

en_buyuk = sayilar[0]
en_kucuk = sayilar[0]
for i in sayilar:
    if i > en_buyuk:
        en_buyuk = i
    if i < en_kucuk:
        en_kucuk = i

print("En büyük sayı : ", en_buyuk)
print("En küçük sayı : ", en_kucuk)

for i in range(len((sayilar))-1):
    for j in range(i+1, len(sayilar)):
        if sayilar[j] > sayilar[i]:
            yedek = sayilar[i]
            sayilar[i] = sayilar[j]
            sayilar[j] = yedek

print(sayilar)
medyan = 0
eleman_sayisi = len(sayilar)
if eleman_sayisi % 2==0:
    print("Eleman Sayısı çift.")
    orta = int((eleman_sayisi/2)-1)
    diger_orta = orta + 1
    
    medyan = (sayilar[orta] + sayilar[diger_orta])/2
    
else:
    orta = int((eleman_sayisi-1)/2)
    medyan = sayilar[orta]

print("Medyan Değeri : ", medyan)
      

# print("-"*100)

# for i in sayilar:
#     for j in sayilar:
#         print(i,j)

